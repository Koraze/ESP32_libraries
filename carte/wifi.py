# Readme #
#
# Variables "publiques"
# - station      : objet wifi
# - hostname     : url (réseau local uniquement)
#
# fonctions "publiques"
# - scan()       : affiche les réseaux wifi proches et visibles 
# - connect(...) : connection à l'une des bornes dans "WIFI_ROUTEURS"
# - connected()  : indique si la carte est connectée en WiFi ou non
# - disconnect() : déconnection
# - init_wifi()  : gestion du WiFi par rapport aux parametres "config"


# Librairies
from network  import WLAN, STA_IF
from time     import sleep
from config   import *


# Fonction : recherche de routeurs proche
def scan():
    print()
    available = station.scan()
    print("Wifi : routeurs visibles proches")
    if len(available) == 0 :
        print("- None")
    else :
        for i in available :
            print("- ", i)

    
# Fonction : Comportement si connecté
def connected() :
    if station.isconnected() == True:
        return True
    return False


# Fonction : déconnexion
def disconnect():
    print("Wifi : Deconnexion ...")
    if connected() :
        station.disconnect()
    station.active(False)


# Fonction : connexion
def connect(routeurs=WIFI_ROUTEURS):
    # Activation du WiFi
    station.active(True)
    
    # Si déjà connecté
    if connected():
        return True
    
    # Si non encore connecté
    for k, v in routeurs.items():
        ip0  = '0.0.0.0'
        ssid = k
        mdp  = v[0]
        
        # Initialisation des paramètres de connexion
        try :
            station.ifconfig("dhcp")
            if len(v) == 5 :
                ip, subnet, gateway, dns = v[1:5]
                if ip != ip0 :
                    station.ifconfig((ip[i], subnet[i], gateway[i], dns[i]))
        
        # Si erreur, une connexion est surement déjà établie
        except :
            if connected():
                return True
        
        # Connexion et attente
        print("\nWifi : Tentative de connexion a", ssid, "...", end="")
        station.connect(ssid, mdp)
        for i in range(10):
            sleep(1) # élément bloquant
            print(".", end="")
            
            # Si connexion établie
            if connected() :
                print()
                return True
            
    # Si aucune connexion n'est établie
    return False


# Lancement de l'ensemble
station  = WLAN(STA_IF)            # Création de l'objet "Station Wi-Fi"
hostname = 'esp32-' + ESP32_ID[8:]


def init_wifi():
    Data = """Wifi :
    - url  : {}.local
    - ip   : {}
    - mask : {}
    - gw   : {}
    - dns  : {}
    """

    if WIFI_CONNECT :
        station.active(True)  # Activation du WiFi
        station.config(dhcp_hostname = hostname)
        scan()                # Scan des routeurs proches
        if connect(WIFI_ROUTEURS) :             # Connexion aux routeurs indiqués dans "routeurs"
            print("\nWifi : Connecté")
            print(Data.format(hostname, *station.ifconfig()))
        else :
            print("\nWifi : Connexion impossible ...")
    else :
        disconnect()          # Deconnexion
