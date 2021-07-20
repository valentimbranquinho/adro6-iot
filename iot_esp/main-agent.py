# Room Agent v0.1.0
# ESP 32
import machine
import utime
import dht

import utils
import wifi

wlan = wifi.do_connect()

agent = utils.Agent()

pir = machine.Pin(14, machine.Pin.IN)
touch = machine.TouchPad(machine.Pin(4))
sensor = dht.DHT11(machine.Pin(17))

# Configure the threshold at which the pin is considered touched
touch.config(500)


print('Room agent is ready!')


def update_sensors():
    try:
        sensor.measure()
    except OSError:
        pass

    agent.update({
        'touch': bool(utils.touch_read(touch) < 450),
        'motion': bool(pir()),
        'temperature': sensor.temperature(),
        'humidity': sensor.humidity(),
    })


def update_sensors_and_post():
    update_sensors()
    agent.post()


# Send sensors data every 30 seconds
tim = machine.Timer(1)
tim.init(period=30000, mode=machine.Timer.PERIODIC,
         callback=lambda t: update_sensors())

while True:
    update_sensors()

    if agent.sensors['touch'] or agent.sensors['motion']:
        agent.post()

        if agent.sensors['touch']:
            utime.sleep(1.5)
        else:
            utime.sleep(0.5)
