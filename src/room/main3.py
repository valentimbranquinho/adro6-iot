import machine
import utime

relay = machine.Pin(5, machine.Pin.OUT)

while True:
    relay(0)
    utime.sleep(5)
    relay(1)
    utime.sleep(5)
