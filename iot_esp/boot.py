import gc
import wifi

import esp
esp.osdebug(None)

gc.collect()

wlan = wifi.connect()  # wait for connection
