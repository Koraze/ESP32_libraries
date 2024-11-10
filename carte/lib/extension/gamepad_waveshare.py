# Librairies
from toolbox.signal   import In, In_Analog, Out_Freq


# Classes
class Gamepad() :
    def __init__(self, pinout):
        Gamepad.A = In(pinout[5],  True)
        Gamepad.B = In(pinout[11], True)
        Gamepad.C = In(pinout[15], True)
        Gamepad.D = In(pinout[14], True)
        Gamepad.E = In(pinout[13], True)
        Gamepad.F = In(pinout[12], True)
        Gamepad.P = In(pinout[8],  True)
        Gamepad.X = In_Analog(pinout[1], 5)
        Gamepad.Y = In_Analog(pinout[2], 5)
        Gamepad.buzzer = Out_Freq(pinout[0])
    
    def update(self) :
        data = {"A":self.A, "B":self.B,
                "C":self.C, "D":self.D,
                "E":self.E, "F":self.F,
                "P":self.P, "X":self.X,
                "Y":self.Y}
        return data


### Test fonctonnement gamepad ###
def gamepad_test(buzzer=True, vibreur=True) :
    from time import sleep
    from extension.pinout import bpibit_pin

    gp = Gamepad(bpibit_pin)

    if buzzer :
        gp.buzzer = gp.X
    print(gp.update(), "    ", end="\r")
    sleep(0.1)
