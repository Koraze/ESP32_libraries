# Readme #
#
# fonctions "publiques"
# - connect(...) : ouverture de l'accès au REPL
# - init_wifi()  : gestion du REPL par rapport aux paramètres "config"


# Librairies
import wifi
import config


# Fonction : connexion
def connect():
    if wifi.connected() :
        import webrepl
        webrepl.start()
        return True
    return False


def init_repl():
    Data = """
    webrepl : {}
    """

    flag = REPL_CONNECT
    if flag :
        flag = connect()
    print(Data.format(flag))
