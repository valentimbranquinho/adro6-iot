import machine
import time

led = machine.Pin(2, machine.Pin.OUT)
touch = machine.TouchPad(machine.Pin(27))
touch.config(500)


def touchRead(touchPad):
    try:
        return touchPad.read()
    except ValueError:
        return 500


while True:
    if touchRead(touch) < 125:
        led.value(1)
        print(touchRead(touch))
        time.sleep(1)
        led.value(0)
        time.sleep(1)
