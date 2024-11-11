# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/modules/module_gamepad_dfrobot.json")


# Libraries
from time import sleep
from modules.microbit.pinout import mbits_pin  # importez la correspondance 
from modules.microbit.gamepad_dfrobot import Gamepad


# Lecture des boutons gamepad
gp = Gamepad(mbits_pin)

while True :
    gp.buzzer  = gp.X
    gp.vibreur = gp.P
    print(gp.read(), end="         \r")
    sleep(0.1)