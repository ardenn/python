import time


class Person:

    def __init__(self, name):
        self.name = name


class Child(Person):
    pass


class Driver(Person):
    pass


class Bus:

    def __init__(self, children=[], drivers=[]):
        self.children = children
        self.drivers = drivers

    def add_driver(self, driver):
        if isinstance(driver, Driver):
            self.drivers.append(driver)
        else:
            try:
                raise ValueError("Not a driver")
            except ValueError:
                print("Not a driver")

    def add_child(self, child):
        if isinstance(child, Child):
            self.children.append(child)
        else:
            try:
                raise ValueError("Not a child")
            except ValueError:
                print("Not a child")

    def drive(self, duration):
        if len(self.drivers) >= 1 and len(self.children) >= 10:
            print("Driving...")
            time.sleep(duration)
            print("Ride ended!")
        else:
            print("Sorry the bus cannot be driven without enough occupants!")

if __name__ == "__main__":
    thebus = Bus()

    for _ in range(2):
        thebus.add_driver(Driver("nana"))

    for _ in range(9):
        thebus.add_child(Child("andrew"))
    thebus.drive(5)

    thebus.add_child(Child("elkana"))
    thebus.drive(5)
