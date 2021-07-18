# -*- coding: utf-8 -*-

import asyncio
import dataclasses
import json
import sys
from typing import Optional

import aiosqlite
import httpx

from iot_api import settings


HTTP_POOL = httpx.AsyncClient(verify=False, limits=httpx.Limits(max_keepalive_connections=5, max_connections=5))


@dataclasses.dataclass
class DBBroker:
    key: str
    ip: str
    port: int

    async def change_state(self, pin, state):
        response = await HTTP_POOL.get(f'http://{self.ip}:{self.port}/?pin{pin}={state}')
        return json.loads(response.read().replace(b"'", b'"'))

    def on(self, pin):
        return self.change_state(pin, 'on')

    def off(self, pin):
        return self.change_state(pin, 'off')


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


@dataclasses.dataclass
class DBMicroController:
    key: str
    broker_key: str
    pin: str
    last_state: Optional[int]

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

    async def toggle(self, broker):
        await self.change_state(broker, self.last_state != 1)


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
                    items.append(DBMicroController(**row))
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
                PRIMARY KEY ("key"),
                CONSTRAINT {MicroController.name}_broker_pin_key UNIQUE (broker_key, pin),
                CONSTRAINT {MicroController.name}_broker_key_fkey FOREIGN KEY (broker_key) REFERENCES "{Broker.name}"(key)
            )""")
        await db.commit()


if __name__ == '__main__' and len(sys.argv) > 1 and sys.argv[1] == 'create_db':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(create_db())
