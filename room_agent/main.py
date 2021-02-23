# Room Agent v0.1.0
# ESP 32

import machine
import ubinascii
import network
import urequests
import ujson
import sys
import utime
import esp32

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('HMI-XF-2G', '3.raparigas#2.rapazes')
while not wlan.isconnected():
    machine.idle() # save power while waiting

led = machine.Pin(15, machine.Pin.OUT)
pir = machine.Pin(14, machine.Pin.IN)
touch = machine.TouchPad(machine.Pin(4))
touch.config(500)               # configure the threshold at which the pin is considered touched
# esp32.wake_on_touch(True)
# machine.lightsleep()
# led.value(0)

url = 'http://192.168.1.65:8000'

agent = {
  'key': ubinascii.hexlify(machine.unique_id()).decode('utf-8'),
  'network': {
    'mac': wlan.config('mac'),
    'ipaddress': wlan.ifconfig()
  }
}

print('Room agent is ready!')

while True:

    agent['sensors'] = {
      'hall': esp32.hall_sensor(),
      'temperature': esp32.raw_temperature(),
      'touch': bool(touch.read() < 500),
      'motion': bool(pir()),
    }

    print(agent)

    if agent['sensors']['touch']:
      post = urequests.post(url, json=agent)
      post.close()
      utime.sleep(0.5)
    elif agent['sensors']['motion']:
      post = urequests.post(url, json=agent)
      post.close()
      utime.sleep(1.5)
    else:
      utime.sleep(0.25)