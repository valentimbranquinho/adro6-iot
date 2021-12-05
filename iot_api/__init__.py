# -*- coding: utf-8 -*-

import asyncio
from collections import defaultdict

from starlette.applications import Starlette
from starlette.background import BackgroundTask
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from iot_api import db


async def log_view(request):
    log = await request.json()

    # Test agent 2462abf3ce58
    if (log['key'] == '2462abf3ce58' and
            log['sensors']['touch'] and
            (log['sensors']['touch'] < 10 or log['sensors']['touch'] > 300 )
        ):
        await pin_view(request, 'kids-wc-light')

    return JSONResponse(log)


async def ping_view(request):
    brokers = await db.Broker.all()
    if brokers:
        await asyncio.gather(*(broker.ping() for broker in brokers))
    return JSONResponse([i.key for i in brokers])


async def pins_view(request):
    controllers = await db.MicroController.all()
    broker_controllers = defaultdict(list)
    for controller in controllers:
        broker_controllers[controller.broker_key].append(controller)

    items = []
    for broker in await db.Broker.all():
        controllers = [
            {
                'key': controller.key,
                'pin': controller.pin,
                'last_state': controller.get_last_state(),
            }
            for controller in broker_controllers[broker.key]
        ]
        if request.query_params.get('only-controllers'):
            items.extend(controllers)
        else:
            items.append({
                'key': broker.key,
                'ip': broker.ip,
                'controllers': controllers,
            })

        # Ping broker
        # Use the first one
        if request.query_params.get('check-alive'):
            controller = broker_controllers[broker.key][0]
            if controller.get_last_state():
                controller.on(broker)
            else:
                controller.off(broker)
            print(
                f'Ping broker {broker.key} using controller pin {controller.pin}')

    return JSONResponse(items)


async def pin_view(request, key=None, force_state=None):
    controller = await db.MicroController.get(key or request.path_params['key'])
    if not controller:
        return JSONResponse('not found')

    broker = await db.Broker.get(controller.broker_key)
    change_to_state = 'off' if controller.last_state else 'on'

    if controller.before_conditions:
        await controller.do_conditions(controller.before_conditions, broker, change_to_state)

    if change_to_state == 'on' or (force_state and force_state == 'on'):
        await controller.on(broker)
    else:
        await controller.off(broker)

    background = None
    if controller.after_conditions:
        background = BackgroundTask(
            controller.do_conditions, controller.after_conditions, broker, change_to_state)

    return JSONResponse(controller.last_state, background=background)


async def startup():
    # Start all active controllers
    active_controllers = await db.MicroController.all(only_active=True)
    if not active_controllers:
        return None

    print(
        f'Starting controllers: {", ".join(i.key for i in active_controllers)}')
    broker_keys = {i.broker_key for i in active_controllers}
    brokers = {i.key: i for i in await db.Broker.all(broker_keys)}
    await asyncio.gather(*(i.on(brokers[i.broker_key]) for i in active_controllers))


class SPAStaticFiles(StaticFiles):
    async def get_response(self, path: str, scope):
        response = await super().get_response(path, scope)
        if response.status_code != 404:
            return response
        else:
            return await super().get_response('index.html', scope)


app = Starlette(
    debug=True,
    routes=[
        Route('/api/log', log_view, methods=['POST']),
        Route('/api/ping', ping_view),
        Route('/api/pins', pins_view),
        Route('/api/pin/{key}', pin_view, methods=['POST']),
        Mount('/', SPAStaticFiles(directory='iot_api/static')),
    ],
    on_startup=[startup])
app = CORSMiddleware(app, allow_origins='*',
                     allow_headers='*', allow_methods='*')
