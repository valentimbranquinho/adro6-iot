from machine import Pin

from time import sleep
import urequests
import network
import uasyncio as asyncio


# wlan = connect_to_wifi.do_connect()

from machine import TouchPad, Pin


# import socket
# addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]

# s = socket.socket()
# s.bind(addr)
# s.listen(1)


@asyncio.coroutine
def serve(reader, writer):
    led.value(0)
    yield from reader.read()
    yield from writer.awrite("HTTP/1.0 200 OK\r\n\r\nHello %s.\r\n" % touch.value())
    yield from writer.aclose()
    sleep(1)
    led.value(1)

loop = asyncio.get_event_loop()
loop.call_soon(asyncio.start_server(serve, "0.0.0.0", 80))
loop.run_forever()
loop.close()

def touchServer():
    url = "https://staging-isotis-site.framework.pt/en/api/entities"
    url = 'http://192.168.1.65:8000'
    r = urequests.get(url) 
    # print(r.content)
    r.close()

# touchServer()

# while True:
#     if touch.value():
#         if touch_on:
#             led.value(1)
#             touch_on = False
#         else:
#             led.value(0)
#             touch_on = True


while True:
    if touch.value():
        led.value(1)
    else:
        led.value(0)

    # cl, addr = s.accept()
    # request = cl.recv(1024)
    # request = str(request)
    # test_get = request.find('/?led=1')
    # if test_get == 6:
    #     touchServer()
    #     led.value(1)
    #     cl.send(str('Cool!' + str(touch.value())))
    # cl.close()