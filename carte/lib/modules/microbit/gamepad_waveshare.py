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

    def read_json(self) :
        data = {"A":self.A, "B":self.B,
                "C":self.C, "D":self.D,
                "E":self.E, "F":self.F,
                "P":self.P, "X":self.X,
                "Y":self.Y}
        return data

    def read(self) :
        data = str(self.A) + str(self.B) + str(self.C) + str(self.D) + 
               str(self.E) + str(self.F) + str(self.P) + " "
               str(self.X) + " " + str(self.Y)
        return data


### Test fonctonnement gamepad (avec une carte mbits) ###
if __name__ == '__main__':
    from time import sleep
    from extension.pinout import mbits_pin

    gp = Gamepad(mbits_pin)

    gp.buzzer  = gp.X
    print(gp.read(), end="         \r")
    sleep(0.1)