# Connect to wifi using ESP32
import network
import machine

WIFI_SSID = 'HMI-XF-2G'
WIFI_PASSWORD = '3.raparigas#2.rapazes'


def connect():
    wlan = network.WLAN(network.STA_IF)

    if wlan.isconnected():
        print("Already connected")
        return wlan

    wlan.active(True)
    wlan.connect(WIFI_SSID, WIFI_PASSWORD)

    while not wlan.isconnected():
        machine.idle()  # save power while waiting

    print('Connection successful')
    print(wlan.ifconfig())

    return wlan
