# Utilities for ESP32
import machine
import ubinascii
import esp32


class Agent:
    def __init__(self):
        self.key = parseUbiCode(machine.unique_id())
        self.type = None
        self.sensors = {
            'hall': 0,
            'board-temperature': 0,
        }

        self.updateSensors()

    def updateSensors(self, moreSensorsData = {}):
        self.sensors['hall'] = esp32.hall_sensor()
        self.sensors['board-temperature'] = (esp32.raw_temperature() - 32) * 5.0/9.0

        if moreSensorsData:
            self.sensors.update(moreSensorsData)

    # def updateNetwork(self, wlan):
    #     self.network['mac'] = parseUbiCode(wlan.config('mac'))
    #     self.network['ifconfig'] = wlan.ifconfig()

def parseUbiCode(code):
  return ubinascii.hexlify(code).decode('utf-8')
