import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
touch = machine.TouchPad(machine.Pin(27))
touch.config(500)


def touch_read(touchpad):
    try:
        return touchpad.read()
    except ValueError:
        return 500


while True:
    if touch_read(touch) < 125:
        led.value(1)
        print(touch_read(touch))
        time.sleep(1)
        led.value(0)
        time.sleep(1)
