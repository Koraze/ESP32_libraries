try :
    from deps.umqtt.robust2  import MQTTClient
except : 
    from umqtt.robust2 import MQTTClient

from tools.watch  import *
from time import sleep


class MQTT_Client():
    def __init__(self, name, ip, port=1883, user=None, password=None, keepalive=30, ssl=False, ssl_params={}, dt=100):
        self.__topic_sub = {}
        self.__topic_pub = {}
        
        self.__c = MQTTClient(name, ip, port=port, keepalive=keepalive, ssl=ssl, ssl_params=ssl_params, user=user, password=password)
        self.__c.set_callback(self.__callback_sub)
        self.__mqtt_init()
        
        self.__mqtt_dt = DT()
        self.update_delai(dt)
        
    ###################### Fonctions privées
    def __mqtt_init(self):
        self.__c.DEBUG         = True   # Print diagnostic messages when retries/reconnects happens
        self.__c.KEEP_QOS0     = False  # Information whether we store unsent messages with the flag QoS==0 in the queue.
        self.__c.NO_QUEUE_DUPS = True   # Option, limits the possibility of only one unique message being queued.
        self.__c.MSG_QUEUE_MAX = 2      # Limit the number of unsent messages in the queue.
    
    def __mqtt_reconnect(self) :             # Gestion de reconnexion
        if self.__c.is_conn_issue():         # If connection errors ...
            while self.__c.is_conn_issue():  # Trying to reconnect
                self.__c.reconnect()
            else :
                self.__c.resubscribe()       # Then resuscribe
    
    def __mqtt_update(self) :        # Mettre à jour la réception / l'envoi des messages MQTT
        # print(self.__c.check_msg(), self.__c.send_queue())
        self.__c.check_msg()         # needed when publish(qos=1), ping(), subscribe()
        self.__c.send_queue()        # needed when using the caching capabilities for unsent messages
    
    def __callback_sub(self, topic, msg, retained, duplicate):
        print(topic, msg)
        if topic in self.__topic_sub :
            for callback in self.__topic_sub[topic] :
                try :
                    callback(topic, msg)
                except Exception as e :
                    print(repr(e))
    
    def __callback_pub(self):
        for topic, watchs in self.__topic_pub.items() :
            for watch in watchs :
                watch.update()
                payload = watch.get_new_value()
                if payload is not None :
                    self.publish(topic, payload)
        
        
    ###################### Fonctions publiques
    def connect(self) :       # Connecter au Broker MQTT
        pass

    def disconnect(self) :    # Déconnecter du Broker MQTT
        print("deconnexion")
        self.__c.disconnect()
        
    def subscribe(self, topic, callback=None) :
        assert type(topic) == str, "must be str"
        assert type(callback) == type(lambda: 0) or callback == None, "must be function"
        
        topic = topic.encode('ascii')
        if topic not in self.__topic_sub :
            self.__topic_sub[topic] = []
            self.__c.subscribe(topic)
        if callback != None :
            self.__topic_sub[topic].append(callback)
            
    def publish(self, topic, payload, callback=None, dt=100):
        assert type(topic)   == str, "must be str"
        assert type(payload) == str, "must be str"
        
        if type(payload) == str :
            if callback == None :
                topic   = topic.encode('ascii')
                payload = payload.encode('ascii')
                
                print("publishing", payload, "in", topic)
                self.__c.publish(topic, payload, qos=1)
            else :
                if topic not in self.__topic_pub :
                    self.__topic_pub[topic] = []
                print("added")
                self.__topic_pub[topic].append(Watch(callback, payload, dt))
    
    def update(self) :
        if self.__mqtt_dt.remaining() <= 0 :
            self.__mqtt_reconnect()
            self.__callback_pub()
            self.__mqtt_update()
            return True
        return False
    
    def update_loop_debug(self) :
        while True:
            self.update()
            
    def update_loop(self) :
        try:
            self.update_loop_debug()
        except Exception as e :
            print(repr(e))    # https://stackoverflow.com/questions/1483429/how-do-i-print-an-exception-in-python
        finally :
            self.disconnect()
    
    def update_delai(self, dt) :
        self.__mqtt_dt.set_pas(max(dt, 100))


# Exemple d'utilisation
def exemple():
    from random import getrandbits
    from config import MQTT_NAME, MQTT_HOST, MQTT_PORT, MQTT_USER, MQTT_PW
    
    def pub_callback():
        temperature = 20 + 0.5*getrandbits(3)
        temperature = round(temperature, 2)
        return temperature
    
    def sub_callback(topic, msg):
        print(msg, "world !")
    
    print(f"Température aléatoire : {pub_callback()}°C")

    mqtt = MQTT_Client(MQTT_NAME, MQTT_HOST, MQTT_PORT)
    mqtt.connect()
    mqtt.update_delai(200)
    mqtt.update()
    mqtt.subscribe("foo_sensor1")
    mqtt.subscribe("foo_sensor2", sub_callback)
    mqtt.publish("foo_sensor2", "hello")
    mqtt.publish("foo_sensor1", '{"temperature" : %.02f}', pub_callback, 10000)
    mqtt.update_loop()
