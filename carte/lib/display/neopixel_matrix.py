from machine import Pin
from neopixel import NeoPixel


class Picture():
    def __init__(self, model, frame, color, size_x, size_y, rotate=0, transparency=0):
        self.model   = model
        self.frame   = frame
        self.color   = color
        self.size_x  = size_x
        self.size_y  = size_y
        self.pixel   = []
        self.create_pixel()
        
    def create_pixel(self):
        for y in range(self.size_y):
            self.pixel.append(list([None] * self.size_x))
            
        for y in range(self.size_y):
            for x in range(self.size_x):
                if self.model == "frame_bit" :
                    x_invert = self.size_x - x - 1
                    self.pixel[y][x] = self.color[(self.frame[y]>>x_invert)&1]
                elif self.model == "frame_char" :
                    self.pixel[y][x] = self.color[int(self.frame[y][x])]
    
    def print(self):
        if self.pixel == []:
            self.create_pixel()
            
        for line in self.pixel :
            print(line)


class Matrix():
    def __init__(self, pin, size_x, size_y, limit=16):
        self.size_x = size_x
        self.size_y = size_y
        self.size   = size_x * size_y
        self.__pin  = Pin(pin, Pin.OUT)
        self.__np   = NeoPixel(self.__pin, self.size)
        self.limit  = limit
    
    def __check_color(self, color):
        for i in range(3) :
            if color[i] > self.limit :
                color[i] = self.limit
            elif color[i] < 0 :
                color[i] = 0
        return color
        
    def __np_write(self, color, x, y):
        position = self.size_y*y + x
        if 0 <= position < self.size :
            self.__np[position] = color
        
    def __rotate(self, rotate, pic, x, y):
        if rotate == 0 :
            xx = x
            yy = y
        elif rotate == 1 :
            xx = pic.size_y-1-y
            yy = x
        elif rotate == 2 :
            xx = pic.size_x-1-x
            yy = pic.size_y-1-y
        else :
            xx = y
            yy = pic.size_x-1-x
        return xx, yy
    
    def fill(self, color=[0, 0, 0]):
        color = self.__check_color(color)
        self.__np.fill(color)
        
    def write(self, pic, start_x=0, start_y=0, rotate=0, transparency=False):
        for color in pic.color :
            self.__check_color(color)
        
        for y in range(pic.size_y) :
            for x in range(pic.size_x) :
                color = pic.pixel[y][x]
                if not transparency or color != [0, 0, 0]:
                    xx, yy = self.__rotate(rotate, pic, x, y)
                    xx, yy = xx+start_x, yy+start_y
                    self.__np_write(color, xx, yy)

    def show(self):
        self.__np.write()


if __name__ == '__main__':
    from time import sleep
    
    pic1 = Picture(model  = "frame_bit",
                   frame  = [0b00001, 0b00010, 0b00001, 0b00001, 0b00001],
                   color  = [[0, 0, 0], [4, 0, 0]],
                   size_x = 5,
                   size_y = 5)

    pic2 = Picture(model  = "frame_char",
                   frame  = ["00001", "00010", "00002", "00002", "00002"],
                   color  = [[0, 0, 0], [4, 0, 0], [0, 4, 0]],
                   size_x = 5,
                   size_y = 5)

    matrix = Matrix(13, 5, 5)
    matrix.fill([4, 0, 0])
    matrix.show()
    sleep(1)

    matrix.write(pic1)
    matrix.show()
    sleep(1)

    matrix.fill()
    for i in range(4) :
        matrix.write(pic2, transparency=True, rotate=i)
        matrix.show()
        sleep(1)

