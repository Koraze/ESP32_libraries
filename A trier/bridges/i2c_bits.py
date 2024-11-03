from random import randint
from .i2c_device import RWbase


class RWBits(RWbase):
    def __init__(self, register: int, lowest_bit: int, nb_bits: int=1, nb_bytes: int=1, lsb_first: bool=True) -> None:
        self._reg        = register
        self._mask       = ((1 << nb_bits) - 1) << lowest_bit
        self._mask_      = ~self._mask
        self._buf        = bytearray(nb_bytes)
        self._lowest_bit = lowest_bit
        self._lsb_first  = lsb_first
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
        
        reg   = 0
        order = range(len(self._buf)-1,-1,-1) if self._lsb_first else range(len(self._buf))
            
        for i in order:
            reg = (reg << 8) | self._buf[i]
        reg = (reg & self._mask) >> self._lowest_bit
        return reg

    def __set__(self, obj, value: int) -> None:
        self._read(obj)
        
        reg   = 0
        order = range(len(self._buf)-1,-1,-1) if self._lsb_first else range(len(self._buf))
        for i in order:
            reg = (reg << 8) | self._buf[i]

        reg &= self._mask_
        reg |= (value << self._lowest_bit)

        order = reversed(order)
        for i in order:
            self._buf[i] = reg & 0xFF
            reg >>= 8
        
        self._write(obj)

        
class ROBits(RWBits):
    def __set__(self, obj, value: int) -> None:
        raise AttributeError()


# Exemple d'utilisation
def exemple():
    class Test:
        value = RWBits(None, 5, nb_bits=4, nb_bytes=2, lsb_first=False)
    
    test = Test()
    test.value
    test.value = 15
    test.value = 14
    test.value = 0