# https://github.com/adafruit/Adafruit_CircuitPython_Register/blob/main/adafruit_register/i2c_bits.py

from random import randint
from .i2c_device import RWbase
import struct


class RWBytes(RWbase):
    def __init__(self, register: int, struct_format: str) -> None:
        self._reg    = register
        self._format = struct_format
        self._buf    = bytearray(struct.calcsize(self._format))
        self._read  = self.__read_i2c
        self._write = self.__write_i2c
        
        if register == None :
            print("debug mode")
            self._read  = self.__show
            self._write = self.__show
            for i in range(len(self._buf)-1, -1, -1):
                self._buf[i] = randint(0, 255)

    def __get__(self, obj, objtype=None) -> int:
        self._read(obj)
        value = tuple(struct.unpack(self._format, self._buf))
        if len(value) == 1 :
            return value[0]
        return value

    def __set__(self, obj, value: int) -> None:
        self._read(obj)
        if type(value) is int :
            struct.pack_into(self._format, self._buf, 0,  value)
        else :
            struct.pack_into(self._format, self._buf, 0, *value)
        self._write(obj)

        
class ROBytes(RWBytes):
    def __set__(self, obj, value: int) -> None:
        raise AttributeError()


# Exemple d'utilisation
def exemple():
    class Test:
        value = RWBytes(None, ">H")
    
    test = Test()
    test.value = (256*10+ 5, )
    test.value = (256*40+20, )