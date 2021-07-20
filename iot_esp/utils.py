# Utilities for ESP32
import machine
import ubinascii
import esp32
import urequests
import ujson

API_URL = 'http://172.16.9.254:8100/api/agent/'


class Agent:
    def __init__(self):
        self.key = parse_ubi_code(machine.unique_id())
        self.sensors = {
            'hall': 0,
            # 'board-temperature': 0,
        }

        self.update()

    def update(self, more_sensors_data={}):
        self.sensors['hall'] = esp32.hall_sensor()
        # self.sensors['board-temperature'] = (
        #     esp32.raw_temperature() - 32) * 5.0/9.0

        if more_sensors_data:
            self.sensors.update(more_sensors_data)

    def post(self):
        try:
            post = urequests.post(API_URL + 'log', json=self.__dict__)
            post.close()
        except:
            pass

    # def updateNetwork(self, wlan):
    #     self.network['mac'] = parseUbiCode(wlan.config('mac'))
    #     self.network['ifconfig'] = wlan.ifconfig()


def parse_ubi_code(code):
    return ubinascii.hexlify(code).decode('utf-8')


def touch_read(touchpad):
    try:
        return touchpad.read()
    except ValueError:
        return 500
