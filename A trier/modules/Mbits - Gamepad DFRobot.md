
[Wiki DFRobot](https://wiki.dfrobot.com/SKU_DFR0536_Micro_bit_Gamepad_Expansion_Board)

![[- 🖼️ Pictures/Embarques/Pinouts/pinout gamepad dfrobot.png]]

```python
from machine import ADC, Pin, PWM

microbit_pin = [26, 32, 25, 13, 27, 36, 5, 12, 4, 34, 14, 39, 15, 18, 19, 23, 2, 21, 22]


class Input() :
    def __init__(self, value, inversion=False):
        self.__pin = Pin(value, Pin.IN)
        self.__inv = inversion
        
    def __get__(self, obj, objtype=None):
        if self.__inv :
            return int(not self.__pin.value())
        return self.__pin.value()


class Output() :
    def __init__(self, value):
        self.__pin = Pin(value, Pin.OUT)
        
    def __get__(self, obj, objtype=None):
        return self.__pin.value()
    
    def __set__(self, obj, val):
        self.__pin.value(val)


class Analog_In() :
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


class Freq_Out() :
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


class Gamepad() :
    A = Input(microbit_pin[5],  True)
    B = Input(microbit_pin[11], True)
    C = Input(microbit_pin[13], True)
    D = Input(microbit_pin[14], True)
    E = Input(microbit_pin[15], True)
    F = Input(microbit_pin[16], True)
    Z = Input(microbit_pin[8],  True)
    X = Analog_In(microbit_pin[1], 5)
    Y = Analog_In(microbit_pin[2], 5)
    vibreur = Output(microbit_pin[12])
    buzzer  = Freq_Out(26)


from time import sleep
gp = Gamepad()
while True :
    gp.buzzer  = gp.X
    gp.vibreur = gp.Z
    value = (gp.A, gp.B, gp.C, gp.D, gp.E, gp.F, gp.Z, gp.vibreur, gp.X, gp.Y)
    print(value, "    ", end="\r")
    sleep(0.1)
```