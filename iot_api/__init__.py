# -*- coding: utf-8 -*-

from collections import defaultdict

from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
from starlette.routing import Route, Mount
from starlette.staticfiles import StaticFiles

from iot_api import db


async def pins_view(request):
    controllers = await db.MicroController.all()
    broker_controllers = defaultdict(list)
    for controller in controllers:
        broker_controllers[controller.broker_key].append(controller)

    items = []
    for broker in await db.Broker.all():
        items.append({
            'key': broker.key,
            'ip': broker.ip,
            'controllers': [
                {
                    'key': controller.key,
                    'pin': controller.pin,
                    'last_state': controller.get_last_state(),
                }
                for controller in broker_controllers[broker.key]
            ],
        })

        # Ping broker
        # Use the first one
        if request.query_params.get('check-alive'):
            controller = broker_controllers[broker.key][0]
            await broker.change_state(controller.pin, controller.get_last_state())
            print(f'Ping broker {broker.key} using controller pin {controller.pin}')

    return JSONResponse(items)


async def pin_view(request):
    controller = await db.MicroController.get(request.path_params['key'])
    if not controller:
        return JSONResponse('not found')

    broker = await db.Broker.get(controller.broker_key)
    await controller.toggle(broker)
    return JSONResponse(controller.last_state)


async def startup():
    # Start all active controllers
    active_controllers = await db.MicroController.all(only_active=True)
    if not active_controllers:
        return None

    print(f'Starting controllers: {", ".join(i.key for i in active_controllers)}')
    broker_keys = {i.broker_key for i in active_controllers}
    brokers = {i.key: i for i in await db.Broker.all(broker_keys)}
    for controller in active_controllers:
        await controller.on(brokers[controller.broker_key])


app = Starlette(
    debug=True,
    routes=[
        Route('/api/pins', pins_view),
        Route('/api/pin/{key}', pin_view, methods=['POST']),
        Mount('/', StaticFiles(directory='iot_api/static')),
    ],
    on_startup=[startup])
app = CORSMiddleware(app, allow_origins='*', allow_headers='*', allow_methods='*')
