# Relay16 Agent v0.1.0
# ESP 32
import machine
import utime

import wifi
import utils


wlan = wifi.connect() # wait for connection

agent = utils.Agent()
agent.updateNetwork(wlan)
agent.updateSensors()

led = machine.Pin(15, machine.Pin.OUT)
pir = machine.Pin(14, machine.Pin.IN)
touch = machine.TouchPad(machine.Pin(4))

touch.config(500) # configure the threshold at which the pin is considered touched
led.value(0)

print('Relay16 agent is ready!')

while True:
    agent.updateSensors({
        'touch': bool(touch.read() < 500),
        'motion': bool(pir()),
    })
    print(agent)

    led.value(1)
    utime.sleep(2)
