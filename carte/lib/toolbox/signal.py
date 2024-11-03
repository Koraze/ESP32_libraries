# Readme #
#
# Classes
# - In()
# - Out()
# - In_Analog()
# - Out_Freq()


# Librairies
from machine import ADC, Pin, PWM


# Classes
class In() :
    def __init__(self, value, inversion=False):
        self.__pin = Pin(value, Pin.IN)
        self.__inv = inversion
        
    def __get__(self, obj, objtype=None):
        if self.__inv :
            return int(not self.__pin.value())
        return self.__pin.value()


class Out() :
    def __init__(self, value):
        self.__pin = Pin(value, Pin.OUT)
        
    def __get__(self, obj, objtype=None):
        return self.__pin.value()
    
    def __set__(self, obj, val):
        self.__pin.value(val)


class In_Analog() :
    def __init__(self, value, buffer = 1):
        self.__adc = ADC(Pin(value))
        self.__adc.atten(ADC.ATTN_11DB)
        self.__adc.width(ADC.WIDTH_12BIT)
        self.__buff = [0] * buffer
        
    def __get__(self, obj, objtype=None):
        val = self.__adc.read() - 2048
        self.__buff.append(val)
        self.__buff.pop(0)
        return int(sum(self.__buff) / len(self.__buff))


class Out_Freq() :
    def __init__(self, value):
        self.__pwm = PWM(Pin(value))
        self.__pwm.deinit()
        self.__val = 0
        
    def __get__(self, obj, objtype=None):
        return self.__val
    
    def __set__(self, obj, val):
        val = int(val)
        if val > 0 :
            if not self.__val :
                self.__pwm.init()
                self.__pwm.duty()
            self.__pwm.freq(val)
            self.__val = val
        else :
            self.__pwm.deinit()
            self.__val = 0