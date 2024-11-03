from random import randint
from .i2c_device import RWbase


class RWBit(RWbase):
    def __init__(self, register: int, bit: int, nb_bytes: int=1, lsb_first: bool=True) -> None:
        self._reg   = register
        self._mask  = 1 << (bit % 8)
        self._mask_ = ~self._mask
        self._buf   = bytearray(nb_bytes)
        self._byte  = bit // 8 if lsb_first else nb_bytes - (bit // 8) - 1
        self._read  = self.__read_i2c
        self._write = self.__write_i2c
        
        if register == None :
            print("debug mode")
            self._read  = self.__show
            self._write = self.__show
            for i in range(len(self._buf)-1, -1, -1):
                self._buf[i] = randint(0, 255)

    def __get__(self, obj, objtype=None) -> bool:
        self._read(obj)
        return bool(self._buf[self._byte] & self._mask)

    def __set__(self, obj, value: bool) -> None:
        self._read(obj)
        if value:
            self._buf[self._byte] |= self._mask
        else:
            self._buf[self._byte] &= self._mask_
        self._write(obj)

        
class ROBit(RWBit):
    def __set__(self, obj, value: bool) -> None:
        raise AttributeError()


# Exemple d'utilisation
def exemple():
    class Test:
        value = RWBit(None, 3, nb_bytes = 2)
    
    test = Test()
    test.value = True
    test.value = False