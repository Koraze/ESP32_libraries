from bridges.mqtt import MQTT_Client
from config import ESP32_ID, MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PW

# Modification des parametres de connexion
MQTT_HOST = "broker.hivemq.com"
MQTT_PORT = 1883
MQTT_USER = None
MQTT_PW   = None

# Fonctions callback de test
from random import getrandbits
def pub_callback():
    temperature = 20 + 0.5*getrandbits(3)
    temperature = round(temperature, 2)
    return temperature

def sub_callback(topic, msg):
    print(msg, "world !")

# Paramétrage de notre client MQTT
mqtt = MQTT_Client(ESP32_ID, MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PW)
mqtt.connect()
mqtt.subscribe("foo_sensor1")
mqtt.subscribe("foo_sensor2", sub_callback)
mqtt.publish("foo_sensor2", "hello")
mqtt.publish("foo_sensor1", '{"temperature" : %.02f}', pub_callback, 5000)

# MaJ de notre client MQTT
while True :
    mqtt.update()