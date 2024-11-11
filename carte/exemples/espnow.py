# Installez d'abord les éléments suivants
# import mip
# mip.install("github:Koraze/ESP32_libraries/mip/bridges/bridge_espnow.json")


# libraries
from bridge.espnow import ESPNOW


# Création d'un objet ESPNOW
e = ESPNOW()


# Partie 1 : Emission de messages (Supprimez la partie non souhaitée)
for i in range(100):
    msg_send = "hello " + str(i)
    e.send(msg_send, None, False)
    print("Sending :", msg_send)


# Partie 2 : Réception de messages (Supprimez la partie non souhaitée)
while True :
    msg_read = e.read(False)
    if msg_read :
        print("Receiving :", msg_send)
