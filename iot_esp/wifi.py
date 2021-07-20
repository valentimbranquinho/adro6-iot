# Connect to wifi using ESP32
import network
import machine

WIFI_SSID = 'adro6.iot'
WIFI_PASSWORD = 'i8MV7ZUmY$MDfHb%Jio'


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('Connecting to network...')
        wlan.connect(WIFI_SSID, WIFI_PASSWORD)
        while not wlan.isconnected():
            pass
    print('Network config:', wlan.ifconfig())

