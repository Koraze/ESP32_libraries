# Identifiant carte
from machine import unique_id
ESP32_ID = ''.join('{:02x}'.format(b) for b in unique_id())

# Liste des routeurs sur lesquels se connecter
WIFI_ROUTEURS = { # Nom : [mot de passe, ip, sous réseau, passerelle, dns]  
    'SSID_1' : ['motdepasse'], 
    'SSID_2' : ['motdepasse', 'ip', 'masque', 'passerelle', 'dns'],
}
WIFI_CONNECT = True
REPL_CONNECT = False

# Parametres broker MQTT
MQTT_HOST = None
MQTT_PORT = None
MQTT_USER = None
MQTT_PW   = None


# --- A réarranger
from machine  import Pin
from time     import sleep
from neopixel import NeoPixel

# Alimentation de la LED NeoPixel embarquée
led_pin = Pin(21, Pin.OUT)
np_pin  = Pin(33, Pin.OUT)
np      = NeoPixel(np_pin, 1)

# Allumer la LED.
def light(a, b, c):
    led_pin.on()
    np[0] = (a, b, c)
    np.write()
    sleep(1)
    np[0] = (0, 0, 0)
    np.write()
    led_pin.off()
    