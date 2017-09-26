class Egg:

    def __init__(self, color, is_broken=False):
        self.color = color
        self.__is_broken = is_broken

    def crack(self):
        self.__is_broken = True

    def __repr__(self):
        return self.color


class EggCarton:

    def __init__(self, eggs=[]):
        self.eggs = eggs

    def add_egg(self, egg):
        self.eggs.append(egg)

    def drop_egg(self):
        self.eggs.pop().crack()

    def display_eggs(self):
        for egg in self.eggs:
            print(egg)

if __name__ == "__main__":
    carton = EggCarton()

    for _ in range(3):
        carton.add_egg(Egg("blue"))
    for _ in range(4):
        carton.add_egg(Egg("yellow"))
    carton.display_eggs()
    carton.drop_egg()
    carton.display_eggs()
