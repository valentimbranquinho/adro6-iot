## Instalar

- Instalar drivers ESP32 Silabs CP210x USB to UART Bridge VCP Drivers

  pip install esptool

http://docs.micropython.org/en/latest/esp32/quickref.html#capacitive-touch

## ESP32

Para ligar ao ESP32 e começar a fazer o reset, é preciso carregar no botão de boot...

    esptool.py --port /dev/tty.SLAB_USBtoUART erase_flash
    esptool.py --chip esp32 --port /dev/tty.SLAB_USBtoUART --baud 460800 write_flash -z 0x1000 esp32/micropython/esp32-idf3-20210202-v1.14.bin

Interagir com Micropython:

    screen /dev/tty.SLAB_USBtoUART 115200

    ampy --port /dev/tty.SLAB_USBtoUART ls
    ampy --port /dev/tty.SLAB_USBtoUART put main.py
    ampy --port /dev/tty.SLAB_USBtoUART rm main.py
    ampy --port /dev/tty.SLAB_USBtoUART get main.py

    ampy --port /dev/tty.SLAB_USBtoUART run --no-output main.py
    ampy --port /dev/tty.SLAB_USBtoUART run main.py

    screen /dev/tty.SLAB_USBtoUART 115200

# PIR Motion Sensor

https://www.instructables.com/Microwave-Vs-PIR-Motion-Sensor-With-ESP32-LoRa-Pro/
https://blog.asksensors.com/connect-pir-motion-sensor-esp32-mqtt/

PIR VCC to ESP32 dev board 5V
PIR GND to ESP32 GDN
PIR DATA to ESP32 GPIO through a 1K Resistor (D2 in this tutorial).

# Notas

    # check if the device woke from a deep sleep
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print('woke from a deep sleep')
    # put the device to sleep for 10 seconds
    machine.deepsleep(10000)
