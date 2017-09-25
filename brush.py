import time


class Toothbrush:

    def __init__(self, color, toothpaste=None):
        self.color = color

    def add_toothpaste(self, toothpaste):
        self.toothpaste = toothpaste

    def brush(self, teeth, seconds):
        time.sleep(seconds)
        print("finished brushing")

    def __repr__(self):
        return self.color


class ElectricToothbrush(Toothbrush):

    def __init__(self, color, toothpaste=None):
        super().__init__(color, toothpaste)
        self.__is_on = False

    def turn_on(self):
        self.__is_on = True

    def turn_off(self):
        self.__is_n = False

    def brush(self, teeth, time):
        if not self.__is_on:
            raise MemoryError("Forgot to turn the Toothbrush on")
        super().brush(teeth, time)

# mytb = Toothbrush("green", toothpaste="colgate")
# print(mytb)
# myetb = ElectricToothbrush("blue", toothpaste="colgate")
# print(myetb)
yellow = ElectricToothbrush("yellow")
# print(yellow)
# eyram = Toothbrush("purple", "sensodyne")
# print(eyram)
# #eyram.brush("teeth", 5)
#yellow.brush("teeth", 1)
yellow.turn_on()
yellow.brush("teeth", 1)
