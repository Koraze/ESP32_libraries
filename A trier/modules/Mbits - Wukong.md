
![[- 🖼️ Pictures/Embarques/Modules/extension elecfreaks 2.avif]]

![[- 🖼️ Pictures/Embarques/Modules/extension elecfreaks.png]]

[Wiki officiel](https://wiki.elecfreaks.com/en/microbit/expansion-board/wukong/)
[Code source TypeScript](https://github.com/elecfreaks/pxt-wukong/blob/master/main.ts)

```
# Ecrit ton programme ici ;-)
from machine  import I2C, Pin
from time import sleep
WUKONG_ADDR = 0x10

class WUKONG(object):

    def __init__(self, i2c):
        self.i2c = i2c


    def set_light_breath(self, br: bool):
        if br:
            self.i2c.writeto(WUKONG_ADDR, bytearray([0x11, 0, 0, 0]))
            sleep(0.1)
            self.i2c.writeto(WUKONG_ADDR, bytearray([0x12, 150, 0, 0]))
        else:
            self.i2c.writeto(WUKONG_ADDR, bytearray([0x12, 0, 0, 0]))
            sleep(0.1)
            self.i2c.writeto(WUKONG_ADDR, bytearray([0x11, 160, 0, 0]))


    def set_light_breath2(self, br: bool):
        if br:
            self.i2c.writeto_mem(WUKONG_ADDR, 0x11, bytearray([0, 0, 0]))
            sleep(0.1)
            self.i2c.writeto_mem(WUKONG_ADDR, 0x12, bytearray([150, 0, 0]))
        else:
            self.i2c.writeto_mem(WUKONG_ADDR, 0x12, bytearray([0, 0, 0]))
            sleep(0.1)
            self.i2c.writeto_mem(WUKONG_ADDR, 0x11, bytearray([160, 0, 0]))


i2c = I2C(0, scl=Pin(21), sda=Pin(22), freq=100000)
print(i2c.scan())

wukong = WUKONG(i2c)
wukong.set_light_breath(True)

```

```python
from micropython import const
from bridges.i2c_bytes  import RWBytes, ROBytes
from bridges.i2c_bit    import RWBit,   ROBit
from bridges.i2c_bits   import RWBits,  ROBits
from bridges.i2c_device import I2C_device
from time import sleep

from micropython import const
from i2c_manage.i2c_bytes  import RWBytes
from i2c_manage.i2c_device import I2C_device
from time import sleep


class WUKONG:
    
    __struct = ">BBB"
    __motor1 = RWBytes(0x01, __struct)
    __motor2 = RWBytes(0x02, __struct)
    __servo0 = RWBytes(0x03, __struct)
    __servo1 = RWBytes(0x04, __struct)
    __servo2 = RWBytes(0x05, __struct)
    __servo3 = RWBytes(0x06, __struct)
    __servo4 = RWBytes(0x07, __struct)
    __servo5 = RWBytes(0x08, __struct)
    __servo6 = RWBytes(0x09, __struct)
    __servo7 = RWBytes(0x09, __struct)
    __lightA = RWBytes(0x11, __struct)
    __lightB = RWBytes(0x12, __struct)
    
    __motor = [__motor1, __motor2]
    __servo = [__servo0, __servo1, __servo2, __servo3, __servo4, __servo5, __servo6, __servo7]
    __light = [__lightA, __lightB]

    
    def __init__(self, i2c: I2C, addr: int = 0x10) -> None:
        self.i2c_device = I2C_device(i2c, addr)
    
    
    def motor_set(self, motor, speed):
        if not (-100 <= speed <= 100) : raise ValueError('speed : [-100, 100]')
        if not (   1 <= motor <=   2) : raise ValueError('motor : 1, 2')
        
        direction = 1 + (speed < 0)
        speed     = int(abs(speed))
        motor     = int(motor) - 1
        self.__motor[motor].__set__(self, (direction, speed, 0))
    
    
    def servo_set(self, servo, angle):
        if not (0 <= servo <=   7) : raise ValueError('servo : [0, 7]')
        if not (0 <= servo <= 180) : raise ValueError('angle : [0, 180]')
        
        servo = int(servo)
        angle = int(angle)
        self.__servo[servo].__set__(self, (angle, 0, 0))
    
    
    def servo_stop(self):
        for i in range(8) :
            self.__servo[i] = (90, 0, 0)
    
    
    def light_set(self, mode, light = 0):
        if mode :
            self.__lightA = (    0, 0, 0); sleep(0.1)
            self.__lightB = (  150, 0, 0)
        else :
            self.__lightB = (light, 0, 0); sleep(0.1)
            self.__lightA = (  160, 0, 0)


if __name__ == '__main__':
    from machine import I2C, Pin
    from neopixel import NeoPixel
    
    i2c = I2C(0, scl=Pin(21), sda=Pin(22), freq=100000)
    wk = WUKONG(i2c)
    for i in range(8) :
        wk.servo_set(i, 180)
    
    np = NeoPixel(Pin(2, Pin.OUT), 4)
    for i in range(0, 4):
        np[i] = (0, 0, 30)
    np.write()

```