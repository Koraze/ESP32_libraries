# Librairies
from toolbox.signal   import In, In_Analog, Out, Out_Freq


# Classes
class Gamepad() :
    def __init__(self, pinout):
        self.A = In(pinout[5],  True)
        self.B = In(pinout[11], True)
        self.C = In(pinout[13], True)
        self.D = In(pinout[14], True)
        self.E = In(pinout[15], True)
        self.F = In(pinout[16], True)
        self.P = In(pinout[8],  True)
        self.X = In_Analog(pinout[1], 5)
        self.Y = In_Analog(pinout[2], 5)
        self.buzzer  = Out_Freq(26)
        self.vibreur = Out(pinout[12])
    
    def update(self) :
        data = {"A":self.A, "B":self.B,
                "C":self.C, "D":self.D,
                "E":self.E, "F":self.F,
                "P":self.P, "X":self.X,
                "Y":self.Y}
        return data


### Test fonctonnement gamepad (avec une carte mbits) ###
def gamepad_test(buzzer=True, vibreur=True) :
    from time import sleep
    from extension.pinout import mbits_pin

    gp = Gamepad(mbits_pin)

    if buzzer :
        gp.buzzer  = gp.X
    if vibreur :
        gp.vibreur = gp.P
    print(gp.update(), "    ", end="   \r")
    sleep(0.1)