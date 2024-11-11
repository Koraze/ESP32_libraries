from .thread import Thread

class MEAN():
    def __init__(self, dt, fct, start=True, debug=False):
        self.__fct    = fct
        self.__value  = 0
        self.__number = 0
        self.__thread = Thread(self.__update, dt)
        self.__debug  = debug
        if start :
            self.start()
        
    def state(self):
        return self.__thread.state
    
    def reset(self):
        self.__value  = 0
        self.__number = 0
        
    def start(self):
        self.__thread.start()
        
    def stop(self):
        self.__thread.stop()
    
    def output(self, reset=True):
        data = self.__value
        if reset :
            self.reset()
        return data
    
    def __update(self):
        data = float(self.__fct())
        if data :
            self.__number += 1
            number = float(self.__number)
            self.__value  *= (number - 1.0) / number
            self.__value  += data / number
        if self.__debug :
            print(data, self.__value)


# Exemple d'utilisation
def exemple():
    from time import sleep
    
    count = 0
    def essai():
        global count
        count += 1
        return count
    
    """
    print("start")
    moyenne = MEAN(1000, essai, debug=True)
    sleep(5)
    moyenne.stop()
    """
    
    print("st")
    moyenne = MEAN(1000, essai, debug=False)
    for i in range(5):
        print(moyenne.output(False))
        sleep(1)
    moyenne.stop()
