import machine
import network
import urequests
import sys
import utime
import esp32

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('HMI-XF-2G', '3.raparigas#2.rapazes')
while not wlan.isconnected():
    machine.idle() # save power while waiting

led = machine.Pin(15, machine.Pin.OUT)
touch = machine.TouchPad(machine.Pin(4))
touch.config(500)               # configure the threshold at which the pin is considered touched
esp32.wake_on_touch(True)

led.value(0)

url = 'http://192.168.1.65:8000'

machine.lightsleep()

while True:
    print('Touch: ', touch.read())
    if touch.read() < 500:
        led.value(1)
        post = urequests.post(url)
        print(post.content)
    else:
        led.value(0)
    
    utime.sleep(1)