class Apple:
    price = 5
    created_apples = 0

    def __init__(self, color):
        Apple.created_apples += 1

        if Apple.created_apples % 12 == 0:
            self.color = "brurple"
        elif Apple.created_apples == 3:
            self.color = "purple"
        elif Apple.created_apples == 4:
            self.color = "brown"
        else:
            self.color = color
            self.price = Apple.price

    @classmethod
    def change_price(cls, new_price):
        cls.price = new_price

    def __repr__(self):
        return "This is a {:.0f} cedi {} Apple".format(self.price, self.color)

if __name__ == "__main__":
    # first = Apple("red")
    # print(first)
    # second = Apple("blue")
    # print(second)
    # Apple.change_price(6.0)
    # third = Apple("green")
    # print(third)
    # print(first)
    for _ in range(30):
        print(Apple("red"))
