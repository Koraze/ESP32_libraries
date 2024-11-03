# Librairies
from toolbox.signal   import In, In_Analog, Out_Freq


# Classes
class Gamepad() :
    def __init__(self, pinout):
        self.A = In(pinout[5],  True)
        self.B = In(pinout[11], True)
        self.C = In(pinout[15], True)
        self.D = In(pinout[14], True)
        self.E = In(pinout[13], True)
        self.F = In(pinout[12], True)
        self.P = In(pinout[8],  True)
        self.X = In_Analog(pinout[1], 5)
        self.Y = In_Analog(pinout[2], 5)
        self.buzzer = Out_Freq(26)
    
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
    from extension.pinout import mbits_pin

    gp = Gamepad()

    if buzzer :
        gp.buzzer = gp.X
    print(gp.update(), "    ", end="\r")
    sleep(0.1)
