# Connect to wifi using ESP32
import network
import machine

WIFI_SSID = 'adro6.iot'
WIFI_PASSWORD = 'i8MV7ZUmY$MDfHb%Jio'


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
