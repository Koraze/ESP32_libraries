# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from wifi import init_wifi
from config import light


light(0, 255, 0)
init_wifi()
light(0, 255, 0)