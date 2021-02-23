# Room Agent v0.1.0
# ESP 32
import machine
import urequests
import ujson
import utime
import esp32

import utils
import wifi


API_URL = 'http://192.168.1.65:8000'

wlan = wifi.connect() # wait for connection

agent = utils.Agent()

led = machine.Pin(15, machine.Pin.OUT)
pir = machine.Pin(14, machine.Pin.IN)
touch = machine.TouchPad(machine.Pin(4))

touch.config(500) # configure the threshold at which the pin is considered touched
led.value(0)

print('Room agent is ready!')

def postAgentData():
    try:
        post = urequests.post(url, json=agent.__dict__)
        post.close()
    except:
        pass

    print(agent.__dict__)


# Send sensors data every 15 seconds
tim = machine.Timer(1)
tim.init(period=15000, mode=machine.Timer.PERIODIC, callback=lambda t: postAgentData())

while True:
    agent.updateSensors({
        'touch': bool(touch.read() < 500),
        'motion': bool(pir()),
    })

    if agent.sensors['touch'] or agent.sensors['motion']:
        postAgentData()
        led.value(1)
        utime.sleep(1)

