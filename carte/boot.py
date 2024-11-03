# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
from wifi import init_wifi

init_wifi()
