# Librairies
from extension.pinout import microbit_pin
from toolbox.signal   import In, In_Analog, Out, Out_Freq


# Classes
class Gamepad() :
    A = In(microbit_pin[5],  True)
    B = In(microbit_pin[11], True)
    C = In(microbit_pin[13], True)
    D = In(microbit_pin[14], True)
    E = In(microbit_pin[15], True)
    F = In(microbit_pin[16], True)
    P = In(microbit_pin[8],  True)
    X = In_Analog(microbit_pin[1], 5)
    Y = In_Analog(microbit_pin[2], 5)
    buzzer  = Out_Freq(26)
    vibreur = Out(microbit_pin[12])
    
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
    gp = Gamepad()

    if buzzer :
        gp.buzzer  = gp.X
    if vibreur :
        gp.vibreur = gp.P
    print(gp.update(), "    ", end="   \r")
    sleep(0.1)