## ESP8266

Para ligar ao ESP8266 e começar a fazer o reset, é preciso carregar no botão de boot...

    esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
    esptool.py --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash --flash_size=detect 0 micropython/esp8266-20210202-v1.14.bin

Interagir com Micropython:

    screen /dev/tty.SLAB_USBtoUART 115200

    ampy --port /dev/tty.SLAB_USBtoUART ls
    ampy --port /dev/tty.SLAB_USBtoUART put main.py
    ampy --port /dev/tty.SLAB_USBtoUART rm main.py
    ampy --port /dev/tty.SLAB_USBtoUART get main.py

    ampy --port /dev/tty.SLAB_USBtoUART run --no-output main.py
    ampy --port /dev/tty.SLAB_USBtoUART run main.py

    screen /dev/tty.SLAB_USBtoUART 115200

# Referências

    https://micropython-on-esp8266-workshop.readthedocs.io/en/latest/basics.html

relay pin NodeMCU GPIO NodeMCU physical pin
N1 GPIO16 D0
N2 GPIO5 D1
N3 GPIO4 D2
N4 GPIO0 D3
N5 GPIO2 D4
N6 GPIO14 D5
N7 GPIO12 D6
N8 GPIO13 D7

# -------

# ESP8266 NodeMCU Workshop

Check the [wiki](https://github.com/lvidarte/esp8266/wiki) for the full workshop documentation :)

### Examples

1. [led](https://github.com/lvidarte/esp8266/tree/master/examples/led)
2. [button](https://github.com/lvidarte/esp8266/tree/master/examples/button)
3. [neopixels](https://github.com/lvidarte/esp8266/tree/master/examples/neopixels)
4. [dht11](https://github.com/lvidarte/esp8266/tree/master/examples/dht11)
5. [sdd1306](https://github.com/lvidarte/esp8266/tree/master/examples/sdd1306)
6. [sdcard](https://github.com/lvidarte/esp8266/tree/master/examples/sdcard)
7. [ota](https://github.com/lvidarte/esp8266/tree/master/examples/ota)
8. [ap](https://github.com/lvidarte/esp8266/tree/master/examples/ap)
9. [rgb-lamp](https://github.com/lvidarte/esp8266/tree/master/examples/rgb-lamp)
10. [sg90](https://github.com/lvidarte/esp8266/tree/master/examples/sg90)

### NodeMCU

![nodemcu pinout](https://raw.githubusercontent.com/lvidarte/esp8266/master/nodemcu_pins.png)

### PlatformIO IDE for Atom

PlatformIO IDE is the next-generation integrated development environment for IoT.

- [http://platformio.org](http://platformio.org/)
- [Installation](http://docs.platformio.org/en/latest/ide/atom.html#installation)
- [Getting started with PlatformIO and NodeMCU](https://www.losant.com/blog/getting-started-with-platformio-esp8266-nodemcu)

### Phant IoT Server

Phant is a modular logging tool developed by [SparkFun Electronics](https://www.sparkfun.com/) for collecting data from the Internet of Things. phant is the open source software that powers data.sparkfun.com.

- [http://phant.io/](http://phant.io)
- [https://github.com/sparkfun/phant](https://github.com/sparkfun/phant)

### Libraries

- [Arduino core for ESP8266 WiFi chip](https://github.com/esp8266/Arduino)
- [WifiManager](https://github.com/tzapu/WiFiManager)
- [Phant Arduino](https://github.com/sparkfun/phant-arduino)
- [Phant Python](https://github.com/matze/python-phant)
