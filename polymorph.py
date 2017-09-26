class Person:

    def __init__(self, complaint="no water, too much PHP"):
        self.__complaint = complaint

    def complain(self):
        print(self.__complaint)


class EIT(Person):
    pass


class Fellow(Person):
    pass


class Cat:
    pass

people = list()
people.append(Fellow())
for _ in range(27):
    people.append(EIT())
people.append(Cat())
for person in people:
    if isinstance(person, Person):
        person.complain()
    else:
        print("not a person")
