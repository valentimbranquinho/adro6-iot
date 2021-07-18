from machine import Pin
from utime import sleep

# N1 GPIO16 D0
# N2 GPIO5 D1
# N3 GPIO4 D2
# N4 GPIO0 D3
# N5 GPIO2 D4
# N6 GPIO14 D5
# N7 GPIO12 D6
# N8 GPIO13 D7


def relayOn(relayId):
    Pin(relayId, Pin.OUT)


def relayOff(relayId):
    Pin(relayId, Pin.IN)


while True:
    relayOn(16)
    sleep(1)
    relayOff(16)
    sleep(1)

    relayOn(5)
    sleep(1)
    relayOff(5)
    sleep(1)

    relayOn(4)
    sleep(1)
    relayOff(4)
    sleep(1)

    relayOn(0)
    sleep(1)
    relayOff(0)
    sleep(1)

    relayOn(2)
    sleep(1)
    relayOff(2)
    sleep(1)

    relayOn(14)
    sleep(1)
    relayOff(14)
    sleep(1)

    relayOn(12)
    sleep(1)
    relayOff(12)
    sleep(1)

    relayOn(13)
    sleep(1)
    relayOff(13)
    sleep(1)
