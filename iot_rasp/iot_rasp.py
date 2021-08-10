# Use python 3.6+
# python3.6 -m venv venv
# source venv/bin/activate
# pip install -r requirements.txt
# python iot_rasp.py
# @reboot /home/valentim/adro6/venv/bin/python /home/valentim/adro6/iot_rasp.py >> /tmp/adro6.log &

# Pins 0-8 start high
# More info: https://pinout.xyz/pinout/ground

import json
import time
import RPi.GPIO as GPIO

from urllib.parse import parse_qs
from bottle import route, run, request


RELAY_PINS = range(4, 28)  # last valid pin number is 27

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


def relay_control(pin_id, action):
    if pin_id not in RELAY_PINS:
        return 'off'

    if (action == 'on'):
        GPIO.setup(pin_id, GPIO.OUT, initial=GPIO.HIGH)
    else:
        GPIO.setup(pin_id, GPIO.IN)
        # GPIO.cleanup(pin)

    return action


for pin in RELAY_PINS:
    GPIO.cleanup(pin)
    # relay_control(pin, 'off')


@route('/')
def index():
    params = parse_qs(request.query_string)

    for param, value in params.items():

        if not param.startswith('pin'):
            continue

        pin_id = int(param.replace('pin', ''))
        pin_status_to = value[0]
        pin_status = relay_control(pin_id, pin_status_to)

        return json.dumps({
            'pin': pin_id,
            'action': pin_status,
            'state': pin_status,
        })

    return json.dumps({})


run(host='0.0.0.0', port=8080, server='gunicorn', workers=2)
