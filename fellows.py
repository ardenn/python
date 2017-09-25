class Fellow:

    __number = 0

    def __init__(self, name):
        if Fellow.__number < 4:
            self.name = name
            l.append(self)
            Fellow.__number += 1
        else:
            print("Sorry")
        print(Fellow.__number)
l = []
for i in range(10):
    n = Fellow("hf")
    Fellow.__number = 10
print(Fellow.__number)
print(len(l))
