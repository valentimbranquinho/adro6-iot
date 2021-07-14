# N1 GPIO16 D0 (open)
# N2 GPIO5 D1
# N3 GPIO4 D2
# N4 GPIO0 D3
# N5 GPIO2 D4 (open)
# N6 GPIO14 D5
# N7 GPIO12 D6
# N8 GPIO13 D7

from machine import Pin
from utime import sleep

try:
    import usocket as socket
except:
    import socket


def relay_control(relay_id, action):
    if (action == 'on'):
        pin = Pin(relay_id, Pin.OUT)
    else:
        pin = Pin(relay_id, Pin.IN)

    # Parse value
    return 'on' if not pin.value() else 'off'


# Set open relays to closed on startup
relay_control(16, 'off')
relay_control(2, 'off')


def get_params(request):
    request = str(request)
    raw_params = [i.split('=') for i in request.split("\n")
                  [0].split(" ")[1][2:].split("&")]

    for param in raw_params:
        if len(param) == 2:
            return {
                'pin': int(param[0].replace('pin', '')),
                'action': param[1],
            }
    return {}


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 8080))
s.listen(5)

while True:
    conn, addr = s.accept()

    # print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    data = get_params(request)

    if data:
        data['state'] = relay_control(data['pin'], data['action'])
        sleep(0.25)

    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: application/json\n')
    conn.send('Connection: close\n\n')
    conn.sendall(str(data))

    conn.close()
