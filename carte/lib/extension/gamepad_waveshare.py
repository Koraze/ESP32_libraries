# Librairies
from extension.pinout import mbits_pin
from toolbox.signal   import In, In_Analog, Out_Freq


# Classes
class Gamepad() :
    A = In(mbits_pin[5],  True)
    B = In(mbits_pin[11], True)
    C = In(mbits_pin[15], True)
    D = In(mbits_pin[14], True)
    E = In(mbits_pin[13], True)
    F = In(mbits_pin[12], True)
    P = In(mbits_pin[8],  True)
    X = In_Analog(mbits_pin[1], 5)
    Y = In_Analog(mbits_pin[2], 5)
    buzzer = Out_Freq(26)
    
    def update(self) :
        data = {"A":self.A, "B":self.B,
                "C":self.C, "D":self.D,
                "E":self.E, "F":self.F,
                "P":self.P, "X":self.X,
                "Y":self.Y}
        return data


### Test fonctonnement gamepad ###
def gamepad_test(buzzer = True) :
    from time import sleep
    gp = Gamepad()

    if buzzer :
        gp.buzzer = gp.X
    print(gp.update(), "    ", end="\r")
    sleep(0.1)
