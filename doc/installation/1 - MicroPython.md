

Vous avez devant vous votre carte ESP32 toute neuve. Cependant, votre carte est pour le moment vide et ne peut lancer aucun script Python. Remédions à cela


# 1 - Installation de Thonny
Pour préparer votre carte, il nous faut dans un premier temps un logiciel capable de communiquer avec elle. Le logiciel léger et open-source [Thonny](https://thonny.org/) fera très bien l'affaire :
- Sur le [site officiel](https://thonny.org/), téléchargez la dernière version de Thonny qui vous convient
- Installez le logiciel, puis lancez-le
- Branchez votre carte à votre ordinateur
- Allez dans la première interface *Outils > Options*
- Sélectionnez *MicroPython (ESP32)* dans *Interpreteur*


# 2 - Installation de MicroPython
Ensuite, il vous faut dans un second temps un microgiciel micropython générique ou adapté à votre carte. Vous pouvez trouver des versions de MicroPython :
- Renseignez-vous sur les caractéristiques de votre carte ESP32 (ROM, SPIRAM, ...)
- Allez dans la seconde interface *Outils > Options > Interpreteur > Installer ...*
- Choisissez le microgiciel qui vous convient :
    1. Depuis cette interface (versions génériques)
    2. Depuis le site officiel [micropython](https://micropython.org) (plus de choix)
    3. Depuis le dossier `firmware` de ce répertoire (pas forcément à jour)
- Configurez l'interface en fonction de votre choix
- Cliquez sur *Installer*, puis quittez l'interface une fois l'installation finie


# 3 - Accès à l'interpréteur de l'ESP32 depuis Thonny
Enfin, vérifions que tout fonctionne. Pour cela, nous allons demander à Thonny de nous mettre en relation avec l'interpréteur microPython nouvellement installé sur notre carte ESP32 :
- Restez dans la première interface *Outils > Options > Interpreteur*
- Sélectionnez le port COM de votre carte dans *Port ou WebREPL*
- Quittez la première interface
- Tapez `print("hello")` dans l'onglet *console*


> [!TIP]
> Si la carte vous répond `hello`, Félicitations !
> Votre carte contient un interpréteur python fonctionnel et Thonny arrive à communiquer avec lui.

