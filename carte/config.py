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
