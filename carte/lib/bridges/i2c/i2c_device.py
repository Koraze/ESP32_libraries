from machine import I2C


class I2C_device:
    def __init__(self, i2c: I2C, address: int):
        self._i2c   = i2c
        self._add   = address
        
    def read(self, reg, buf):
        self._i2c.readfrom_mem_into(self._add, reg, buf)
        
    def write(self, reg, buf):
        self._i2c.writeto_mem(self._add, reg, buf)


class RWbase:
    def __read_i2c(self, obj):
        obj.i2c_device.read(self._reg, self._buf)
        
    def __write_i2c(self, obj):
        obj.i2c_device.write(self._reg, self._buf)
    
    def __show(self, obj):
        for i in range(len(self._buf)-1, -1, -1):
            print('{:08b} '.format(self._buf[i]), end="")
        print()