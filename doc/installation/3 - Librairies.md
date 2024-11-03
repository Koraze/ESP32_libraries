

Votre carte peut maintenant lancer des scripts Python et se connecter à internet. On peut donc lui installer quelques librairies pour augmenter son champ d'actions


# 1 - Préparation des fichiers
Pour installer une librairie, il suffit comme pour l'étape [WiFi et config](-%20🚧%20GitHub/ESP32_libraries/doc/installation/2%20-%20WiFi%20et%20config.md) de créer des dossiers et des fichiers dans votre carte au bon endroit. Cependant, il est également possible d'importer certains fichiers directement depuis des *dépôts GitHub* sur Internet à l'aide de `mip.install(...)`
- Assurez-vous d'avoir bien [accès à l'interpréteur de votre carte](-%20🚧%20GitHub/ESP32_libraries/doc/installation/1%20-%20MicroPython.md) depuis Thonny
- Dans la console, je lance la commande `import mip`
- Ensuite, je lance la fonction `mip.install(...)`

Notons que `mip.install(...)` *Expliquer fonctionnement *

```python
# Exemples
# - Installation du support ESPNOW
# - instalaltion du support REPL

import mip
mip.install("github:Koraze/ESP32_libraries/mip/bridge_espnow.json") 
mip.install("github:Koraze/ESP32_libraries/mip/bridge_repl.json")
```


# Librairies MicroPython
```python
import mip
mip.install("github:Koraze/ESP32_libraries/mip/extension_gamepad_waveshare.json")
```



## Installation du client MQTT (basé sur les librairies de fizista)
```python
import mip
mip.install("github:Koraze/ESP32_libraries/mip/bridge_mqtt.json")
```

## Installation des modules i2c (basé sur le travail d'Adafruit)
Les modules actuelement adaptés sont :
- ina219
- max17048

```python
# Remplacez xxxx par le nom du module (exemple ina219)
import mip
mip.install("github:Koraze/ESP32_librairies/mip/module_xxxx.json")
```