from time  import sleep
from .dt   import DT
import _thread


# Classe Thread
class Thread():
    def __init__(self, update, dt=100, exact=False):
        self.dt       = DT(dt)
        self.__state  = False
        self.__update = update
        
    def state(self):
        return self.__state
    
    def stop(self):
        self.__state = False
        
    def start(self):
        self.__state = True
        _thread.start_new_thread(self.__thread, ())

    # Ne pas mettre de prints dans le thread
    # Les prints y sont (très) mal gérés et font planter l'ESP32
    def __thread(self):
        self.dt.reinit(times_up=False)
        while self.__state :
            self.__update()
            """
            try :
                self.__update()
            except :
                self.__state = False
                break
            """
            self.dt.waiting()


# Exemple d'utilisation
def exemple():
    def show():
        print("hello")
        
    exemple = Thread(show, dt=2000)
    exemple.start()
    sleep(6)
    exemple.stop()
