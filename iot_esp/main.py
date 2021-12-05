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
        # 'touch': bool(utils.touch_read(touch) > 100 or utils.touch_read(touch) < 10),
        'touch': utils.touch_read(touch),
        'motion': bool(pir()),
        'temperature': sensor.temperature(),
        'humidity': sensor.humidity(),
    })


def update_sensors_and_post():
    update_sensors()
    agent.post()


# Send sensors data every 240 seconds
tim = machine.Timer(1)
tim.init(period=240000, mode=machine.Timer.PERIODIC,
         callback=lambda t: update_sensors())

MOTION_DETECTED_LOCK = False

while True:
    update_sensors()

    # Reset motion lock
    if not agent.sensors['motion']:
        MOTION_DETECTED_LOCK = False

    if (agent.sensors['touch'] > 250 or agent.sensors['touch'] < 15):
        # or (not MOTION_DETECTED_LOCK and agent.sensors['motion'])):
        agent.post()

        # Avoid multiple posts
        if agent.sensors['motion']:
            MOTION_DETECTED_LOCK = True

        if agent.sensors['touch']:
            utime.sleep(1)
