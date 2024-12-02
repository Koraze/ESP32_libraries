from time    import sleep
from toolbox.timer  import Timer
import _thread


# Classe Thread
class Thread():
    __dict = {}
    
    def stop_all():
        for obj in Thread.__dict.values():
            obj.stop()
        
    def start_all():
        for obj in Thread.__dict.values():
            obj.start()
    
    def __init__(self, name, update, dt=100, exact=True):
        if name in Thread.__dict :
            raise Exception("nom déjà utilisé")
        Thread.__dict[name] = self
        self.error     = ""
        self.__dt      = Timer(dt, exact)
        self.__state   = False
        self.__update  = update
        
    def state(self):
        return self.__state
        
    def start(self):
        if not self.__state :
            _thread.start_new_thread(self.__thread, ())
        
    def stop(self):
        self.__state = False

    # Ne pas mettre de prints dans le thread
    # Les prints y sont (très) mal gérés et font planter l'ESP32
    def __thread(self):
        self.error    = ""
        self.__state  = True
        self.__dt.reinit(times_up=False)
        while self.__state :
            try :
                self.__update()
                self.__dt.waiting()
            except Exception as e:
                self.error   = str(e)
                self.__state = False
                break
        self.__state = False


# Fonctions tests - Exemples d'usage
if __name__ == '__main__':
    # Fonction type
    def show():
        print("hello")
    
    # Création d'un thread sur notre foction
    exemple = Thread("hello", show, dt=2000)
    
    # Lancement puis arrêt du thread
    print("start")
    exemple.start()
    sleep(6)
    exemple.stop()
    
    # Lancement puis arrêt de tous les threads
    print("start all")
    Thread.start_all()
    sleep(6)
    Thread.stop_all()
    