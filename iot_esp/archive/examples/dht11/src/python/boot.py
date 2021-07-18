# Init garbage collector
import gc
gc.collect()

# Connect to WiFi
import network
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('<essid>', '<password>')

while not sta_if.isconnected():
    pass

print("Connected!", sta_if.ifconfig())
