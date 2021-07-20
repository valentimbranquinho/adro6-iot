# -*- coding: utf-8 -*-

import asyncio
import dataclasses
import json
import sys
from typing import List, Optional
from typing_extensions import TypedDict

import aiosqlite
import httpx

from iot_api import settings


HTTP_POOL = httpx.AsyncClient(verify=False, limits=httpx.Limits(max_keepalive_connections=5, max_connections=5))
BROKER_LOCKS = {}


async def delay(microseconds: int, coroutine):
    await asyncio.sleep(microseconds / 1000)
    await coroutine


@dataclasses.dataclass
class DBBroker:
    key: str
    ip: str
    port: int

    async def call(self, query: str):
        lock = BROKER_LOCKS.get(self.key)
        if lock is None:
            lock = BROKER_LOCKS[self.key] = asyncio.Lock()

        async with lock:
            response = await HTTP_POOL.get(f'http://{self.ip}:{self.port}/{query}')
            return json.loads(response.read().replace(b"'", b'"'))

    def ping(self):
        return self.call(f'')

    def on(self, pin):
        return self.call(f'?pin{pin}=on')

    def off(self, pin):
        return self.call(f'?pin{pin}=off')


class Broker:
    name = 'brokers'

    @classmethod
    async def all(cls, keys=None):
        args = []
        query = f'SELECT * FROM {cls.name}'
        if keys:
            query += f' WHERE key IN ({",".join("?" for i in keys)})'
            args.extend(keys)

        items = []
        async with aiosqlite.connect(settings.DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, args) as cursor:
                async for row in cursor:
                    items.append(DBBroker(**row))
        return items

    @classmethod
    async def get(cls, key):
        items = await cls.all([key])
        if items:
            return items[0]


class Condition(TypedDict):
    key: str
    action: str
    on_state: str
    after: Optional[int]


@dataclasses.dataclass
class DBMicroController:
    key: str
    broker_key: str
    pin: str
    last_state: Optional[int]
    before_conditions: Optional[List[Condition]]
    after_conditions: Optional[List[Condition]]

    def get_last_state(self):
        if self.last_state is not None:
            return bool(self.last_state)

    async def change_state(self, broker, activate):
        if activate:
            response = await broker.on(self.pin)
        else:
            response = await broker.off(self.pin)

        new_state = None
        if response['state'] == 'on':
            if self.last_state != 1:
                new_state = 1
        elif self.last_state != 0:
            new_state = 0

        if new_state is not None:
            async with aiosqlite.connect(settings.DB_PATH) as db:
                await db.execute(
                    f'UPDATE {MicroController.name} SET last_state = ? WHERE key = ?',
                    [new_state, self.key])
                await db.commit()
            self.last_state = new_state

    async def on(self, broker):
        await self.change_state(broker, True)

    async def off(self, broker):
        await self.change_state(broker, False)

    async def do_conditions(self, conditions: List[Condition], broker, change_to_state: str):
        conditions = [i for i in conditions if i['on_state'] == change_to_state]
        if not conditions:
            return None

        keys = {i['key'] for i in conditions if i.get('key')}
        controllers = {i.key: i for i in await MicroController.all(keys)} if keys else {}

        keys = {i.broker_key for i in controllers.values()}
        keys.discard(broker.key)
        brokers = {i.key: i for i in await Broker.all(keys)} if keys else {}
        brokers[broker.key] = broker

        futures = []
        for condition in conditions:
            controller = controllers[condition['key']]
            coroutine = getattr(controller, condition['action'])(brokers[controller.broker_key])
            if condition.get('after'):
                futures.append(delay(condition['after'], coroutine))
            else:
                futures.append(coroutine)
        await asyncio.gather(*futures)


class MicroController:
    name = 'micro_controllers'

    @classmethod
    async def all(cls, keys=None, only_active=False):
        query = f'SELECT * FROM {cls.name}'

        args = []
        filters = []
        if only_active:
            filters.append('last_state = 1')
        if keys:
            filters.append(f'key IN ({",".join("?" for i in keys)})')
            args.extend(keys)
        if filters:
            query += f' WHERE {" AND ".join(filters)}'

        items = []
        async with aiosqlite.connect(settings.DB_PATH) as db:
            db.row_factory = aiosqlite.Row
            async with db.execute(query, args) as cursor:
                async for row in cursor:
                    item = DBMicroController(**row)
                    items.append(item)
                    if item.before_conditions:
                        item.before_conditions = json.loads(item.before_conditions)
                    if item.after_conditions:
                        item.after_conditions = json.loads(item.after_conditions)
        return items

    @classmethod
    async def get(cls, key):
        items = await cls.all([key])
        if items:
            return items[0]


async def create_db():
    async with aiosqlite.connect(settings.DB_PATH) as db:
        await db.execute(f"""
            CREATE TABLE IF NOT EXISTS "{Broker.name}" (
                "key" varchar(50) NOT NULL,
                "ip" varchar(50) NOT NULL,
                "port" int NOT NULL,
                PRIMARY KEY ("key"),
                CONSTRAINT {Broker.name}_ip_port_key UNIQUE (ip, port)
            )""")
        await db.execute(f"""
            CREATE TABLE IF NOT EXISTS "{MicroController.name}" (
                "key" varchar(50) NOT NULL,
                "broker_key" varchar(50) NOT NULL,
                "pin" varchar(50) NOT NULL,
                "last_state" int,
                "before_conditions" text,
                "after_conditions" text,
                PRIMARY KEY ("key"),
                CONSTRAINT {MicroController.name}_broker_pin_key UNIQUE (broker_key, pin),
                CONSTRAINT {MicroController.name}_broker_key_fkey FOREIGN KEY (broker_key) REFERENCES "{Broker.name}"(key)
            )""")
        await db.execute("""
            INSERT INTO "brokers" ("key", "ip", "port")
            VALUES
                ('b1-1', '172.16.9.46', '8080'),
                ('b1-2', '172.16.9.68', '8080'),
                ('b2-1', '172.16.9.26', '8080')
            """)
        await db.execute("""
            INSERT INTO "micro_controllers" ("key", "broker_key", "pin", "last_state", "before_conditions", "after_conditions")
            VALUES
                ('corridor-light-1', 'b1-1', '26', '0', NULL, '[{"key":"corridor-light-2","action":"on","on_state":"on","after":1000}]'),
                ('corridor-light-2', 'b1-2', '32', '0', NULL, NULL),
                ('dining-room-lights', 'b2-1', '25', '0', NULL, NULL),
                ('dining-room-table-light', 'b1-2', '4', '0', NULL, NULL),
                ('garage-light-1', 'b1-2', '25', '0', NULL, NULL),
                ('hall-light', 'b1-1', '12', '0', NULL, NULL),
                ('ines-mariana-room-hall-light', 'b2-1', '33', '0', NULL, NULL),
                ('ines-mariana-room-light', 'b2-1', '2', '0', NULL, NULL),
                ('kids-wc-exaust', 'b2-1', '15', '0', NULL, NULL),
                ('kids-wc-light', 'b2-1', '14', '0', NULL, NULL),
                ('kids-wc-window-close', 'b2-1', '18', '0', '[{"key":"kids-wc-window-open","action":"off","on_state":"on"}]', NULL),
                ('kids-wc-window-open', 'b2-1', '17', '0', '[{"key":"kids-wc-window-close","action":"off","on_state":"on"}]', NULL),
                ('kitchen-light-1', 'b1-2', '15', '0', NULL, NULL),
                ('kitchen-light-2', 'b1-1', '14', '0', NULL, NULL),
                ('living-room-light', 'b1-2', '26', '0', NULL, NULL),
                ('office-light', 'b1-2', '27', '0', NULL, NULL),
                ('suite-closet-light', 'b2-1', '5', '0', NULL, NULL),
                ('suite-hall-light', 'b2-1', '32', '0', NULL, NULL),
                ('suite-light', 'b2-1', '16', '0', NULL, NULL),
                ('suite-wc-exaust', 'b2-1', '26', '0', NULL, NULL),
                ('suite-wc-light', 'b2-1', '19', '0', NULL, NULL),
                ('suite-wc-window-close', 'b2-1', '4', '0', '[{"key":"suite-wc-window-open","action":"off","on_state":"on"}]', NULL),
                ('suite-wc-window-open', 'b2-1', '27', '0', '[{"key":"suite-wc-window-close","action":"off","on_state":"on"}]', NULL),
                ('unknown-1-1-0', 'b1-1', '0', '0', NULL, NULL),
                ('unknown-1-1-15', 'b1-1', '15', '0', NULL, NULL),
                ('unknown-1-1-16', 'b1-1', '16', '0', NULL, NULL),
                ('unknown-1-1-17', 'b1-1', '17', '0', NULL, NULL),
                ('unknown-1-1-18', 'b1-1', '18', '0', NULL, NULL),
                ('unknown-1-1-19', 'b1-1', '19', '0', NULL, NULL),
                ('unknown-1-1-2', 'b1-1', '2', '0', NULL, NULL),
                ('unknown-1-1-25', 'b1-1', '25', '0', NULL, NULL),
                ('unknown-1-1-27', 'b1-1', '27', '0', NULL, NULL),
                ('unknown-1-1-32', 'b1-1', '32', '0', NULL, NULL),
                ('unknown-1-1-33', 'b1-1', '33', '0', NULL, NULL),
                ('unknown-1-1-4', 'b1-1', '4', '0', NULL, NULL),
                ('unknown-1-1-5', 'b1-1', '5', '0', NULL, NULL),
                ('unknown-1-2-16', 'b1-2', '16', '0', NULL, NULL),
                ('unknown-1-2-17', 'b1-2', '17', '0', NULL, NULL),
                ('unknown-1-2-18', 'b1-2', '18', '0', NULL, NULL),
                ('unknown-1-2-19', 'b1-2', '19', '0', NULL, NULL),
                ('unknown-1-2-2', 'b1-2', '2', '0', NULL, NULL),
                ('unknown-1-2-33', 'b1-2', '33', '0', NULL, NULL),
                ('unknown-1-2-5', 'b1-2', '5', '0', NULL, NULL),
                ('unknown-2-1-12', 'b2-1', '12', '0', NULL, NULL),
                ('wc-guests-window-close', 'b1-2', '12', '0', '[{"key":"wc-guests-window-open","action":"off","on_state":"on"}]', NULL),
                ('wc-guests-window-open', 'b1-2', '14', '0', '[{"key":"wc-guests-window-close","action":"off","on_state":"on"}]', NULL);
            """)
        await db.commit()


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
