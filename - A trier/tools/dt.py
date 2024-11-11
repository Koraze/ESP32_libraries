# Cette librairie permet de fixer le nombre d'exécutions par secondes via ses méthodes
# - waiting()    - bloquant
# - remaining()  - non bloquant

from time import ticks_ms, sleep_ms

class DT():
    def __init__(self, dt=100, exact=False):
        self.__exact = exact
        self.set_pas(dt)
    
    def set_pas(self, dt):
        self.__dt = max(int(dt), 1)
        self.reinit()
        
    def reinit(self, times_up=True):
        if times_up :
            self.__temps = ticks_ms()
        else :
            self.__temps = ticks_ms() + self.__dt
        
    def __reset(self):
        if self.__exact :
            self.__temps = self.__temps + self.__dt
        else :
            self.__temps = ticks_ms() + self.__dt
        
    def remaining(self):
        tps_restant = self.__temps - ticks_ms()
        if(tps_restant <= 0) :
            self.__reset()
        return tps_restant
        
    def waiting(self):
        tps_restant = self.__temps - ticks_ms()
        if(tps_restant > 0) :
            sleep_ms(tps_restant)
        self.__reset()


# Fonctions tests - Exemples d'usage
def exemple_1():
    timer = DT(500, True)
    timer.set_pas(1000) # Exécution chaque seconde
    timer.reinit()
    while True :
        timer.waiting() # Bloquant
        print("hello")

def exemple_2():
    timer = DT(500)                  # Exécution chaque 0.5s
    while True :
        if timer.remaining() <= 0 :  # Non bloquant
            print("hello")

