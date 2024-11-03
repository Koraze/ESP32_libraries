

Votre carte peut maintenant lancer des scripts Python. Cependant, elle n'est pas encore connectée à votre réseau. Résolvons cela.


# 1 - Préparation des fichiers
Dans un premier temps, enregistrons quelques fichiers script dans notre carte ESP32. Leur rôle sera de connecter votre carte à la borne WiFi enregistrée à chaque (re)démarrage.
- Assurez-vous d'avoir bien [accès à l'interpréteur de votre carte](-%20🚧%20GitHub/ESP32_libraries/doc/installation/1%20-%20MicroPython.md) depuis Thonny 
- Pour chacun des fichiers [boot.py](-%20🚧%20GitHub/ESP32_libraries/carte/boot.py), [wifi.py](-%20🚧%20GitHub/ESP32_libraries/carte/wifi.py), [config.py](-%20🚧%20GitHub/ESP32_libraries/carte/config.py) dans le dossier `carte` :
    - Cliquez sur l'icone *Nouveau Fichier* (🗋) dans Thonny
    - Copiez-y le contenu du fichier
    - Cliquez sur 💾 *(Enregistrer > Appareil MicroPython)*
    - Donnez-lui le même nom que celui du fichier copié (sans oublier le `.py`)


# 2 - Configuration de la carte
Maintenant que les fichiers sont enregistrés dans la carte, indiquons dans le fichier `config.py` le nom (*SSID*) et la clé (*motdepasse*) de votre borne WiFi, notamment les paramètres :
- `WIFI_ROUTEURS` : Peut contenir les identifiants de connexion de plusieurs bornes WiFi
- `WIFI_CONNECT` : Doit être à `True` pour initier une connexion

Pour cela, il suffit de réaliser les opérations suivantes :
- Dans le fichier `config.py` :
    - Modifiez la valeur de `WIFI_CONNECT` pour `True`
    - Modifiez la valeur de `WIFI_ROUTEURS` pour `'SSID' : ['motdepasse'],`
    - Enregistrez vos modifications 💾 *(Enregistrer > Appareil MicroPython)*
- Redémarrez la carte :
    - soit en appuyant sur 🛑 *stop* de Thonny
    - soit en cliquant sur le bouton *reset* de votre carte


> [!tip]
> Si la carte vous répond `hello`, Félicitations !
> Votre carte contient un interpréteur python fonctionnel et Thonny arrive à communiquer avec lui.