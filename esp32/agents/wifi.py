# Connect to wifi using ESP32
import network
import machine


def connect():
  wlan = network.WLAN(network.STA_IF)
  wlan.active(True)

  wlan.connect('HMI-XF-2G', '3.raparigas#2.rapazes')

  while not wlan.isconnected():
      machine.idle() # save power while waiting

  return wlan
