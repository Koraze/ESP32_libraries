# Readme #

#
# méthodes ESPNOW "publiques"
# - add_peer(...) : permet la communication avec l'adresse unicast 'peer' 
# - send(...)     : retourne le prochain message reçu (ou rien)


# Librairies
from network  import WLAN, STA_IF
import espnow
import time
import json


# Fonction : connexion
class ESPNOW():
    multicast = b'\x01\x02\x03\x04\x05\x06'

    def __init__(self):
        sta = WLAN(STA_IF)  
        sta.active(True)
        
        self.e = espnow.ESPNow()
        self.e.active(True)
        try :
            self.e.add_peer(self.multicast)
        except :
            pass
        
    def add_peer(self, peer):
        if peer[0] & 0x01 :
            print("adresse multicast")
        e.add_peer(peer)
    
    def send(self, data, peer=None, json_data=True):
        if json_data :
            data = json.dumps(data)
        else :
            data = str(data)
        if not peer :
            peer = self.multicast
        self.e.send(peer, data, True)
        return peer, data
    
    def read(self, json_data=True):
        if self.e.any():
            host, data = self.e.recv()
            if data:
                if json_data :
                    data = json.loads(data)
                return (host, data)
        return None


### Test émission et réception ###
def test_send() :
    e = ESPNOW()
    for i in range(100):
        e.send(i, None, False)

### Test émission et réception ###
def test_receive() :
    e = ESPNOW()
    while True :
        e.read(False)
