# https://randomnerdtutorials.com/micropython-esp32-esp8266-dht11-dht22-web-server/

import dht
import urequests
import network
from time import sleep

from machine import Pin


sensor = dht.DHT22(Pin(12))

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('mifx.wifi', '9qX!Z2Da5JbD')
while not wlan.isconnected():
    machine.idle() # save power while waiting

# print(wlan.ifconfig())

import socket
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind(addr)
s.listen(5)

def read_sensor():
    global temp, hum
    temp = hum = 0
    try:
      sensor.measure()
      temp = sensor.temperature()
      hum = sensor.humidity()
      if (isinstance(temp, float) and isinstance(hum, float)) or (isinstance(temp, int) and isinstance(hum, int)):
        msg = '{0:3.1f},{1:3.1f}'.format(temp, hum)
  
        # uncomment for Fahrenheit
        #temp = temp * (9/5) + 32.0
  
        hum = round(hum, 2)
        return(msg)
      else:
        return('Invalid sensor readings.')
    except OSError as e:
      return('Failed to read sensor.')

def web_page():
    html = """<!DOCTYPE HTML><html>
    <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        html {
        font-family: Arial;
        display: inline-block;
        margin: 0px auto;
        text-align: center;
        }
        h2 { font-size: 3.0rem; }
        p { font-size: 3.0rem; }
        .units { font-size: 1.2rem; }
        .dht-labels{
        font-size: 1.5rem;
        vertical-align:middle;
        padding-bottom: 15px;
        }
    </style>
    </head>
    <body>
    <h2>ESP DHT Server</h2>
    <p>
        <i class="fas fa-thermometer-half" style="color:#059e8a;"></i> 
        <span class="dht-labels">Temperature</span> 
        <span>"""+str(temp)+"""</span>
        <sup class="units">&deg;C</sup>
    </p>
    <p>
        <i class="fas fa-tint" style="color:#00add6;"></i> 
        <span class="dht-labels">Humidity</span>
        <span>"""+str(hum)+"""</span>
        <sup class="units">%</sup>
    </p>
    </body>
    </html>"""
    return html

while True:
    # d = dht.DHT22(sensor)
    # print(d.measure())
    cl, addr = s.accept()
    request = cl.recv(1024)
    sensor_readings = read_sensor()
    print(sensor_readings)
    response = web_page()
    cl.send('HTTP/1.1 200 OK\n')
    cl.send('Content-Type: text/html\n')
    cl.send('Connection: close\n\n')
    cl.sendall(response)
    cl.close()
    
