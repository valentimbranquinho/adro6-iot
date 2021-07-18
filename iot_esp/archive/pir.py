from machine import Pin
from time import sleep

# motion = False

#def handle_interrupt(pin):
#    global motion
#    motion = True
#    global interrupt_pin
#    interrupt_pin = pin 

led = Pin(2, Pin.OUT)
relay = Pin(4, Pin.OUT, value=1)

pir = Pin(12, Pin.IN)
light_sensor = Pin(14, Pin.IN)

# pir.irq(trigger=Pin.IRQ_RISING, handler=handle_interrupt)

def changeStateLedOutput():
    for x in range(10):
        led.value(0)
        sleep(0.05)
        led.value(1)
        sleep(0.05)

changeStateLedOutput()

while True:
    if light_sensor.value():
        if pir.value():
            print('Motion detected in a dark room')
            led.value(0)
            print('Open relay')
            relay.value(0)
            sleep(30)
            led.value(1)
        else:
            led.value(1)
            relay.value(1)
    else:
        led.value(1)
        relay.value(1)
    sleep(1)