# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/modules/module_base_wukong.json")


# Libraries
from machine import Pin, I2C
from time import sleep

# Ouverture du port I2C
i2c = I2C(1, scl=Pin(21), sda=Pin(22), freq=100000)

# Boucle principale
while True :
    print(i2c.scan())  # Scan de l'ensemble du réseau CAN
    sleep(1)           # Attendre 1 seconde