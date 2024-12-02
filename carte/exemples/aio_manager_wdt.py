# Installez d'abord les éléments suivants
# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/toolbox/aio_manager.json")
# 
# Pour plus d'informations : https://github.com/micropython/micropython-lib/tree/master/micropython/aiorepl


# libraries
from toolbox.aio_manager import aio_manager
from machine             import Pin


led = Pin(5, Pin.OUT)
def blink():
    led.value(not led.value())


from machine import WDT
wdt = WDT(timeout=4000)
aio_manager.add("watchdog", wdt.feed, 400)
aio_manager.add("test", led, 1000)
asyncio.run(main())
