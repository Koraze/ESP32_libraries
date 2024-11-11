# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/modules/module_base_wukong.json")


# Libraries
from time import sleep
from modules.microbit.pinout import mbits_pin  # importez la correspondance 
from modules.microbit.base_wukong import WUKONG


# Lecture des boutons gamepad
from machine import I2C, Pin
from neopixel import NeoPixel
from time import sleep

i2c = I2C(0, scl=Pin(21), sda=Pin(22), freq=100000)
wk = WUKONG(i2c)

wk.light_set(False, True)
sleep(2)
wk.light_set(False, False)

for i in range(8) :
    wk.servo_set(i, 180)

np = NeoPixel(Pin(2, Pin.OUT), 4)
for i in range(0, 4):
    np[i] = (0, 0, 30)
np.write()