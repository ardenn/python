class Person:

    def __init__(self, name, gender):
        if(name == "Francis"):
            raise ValueError(
                "What kind of horrible parent would name their child Francis?")
        else:
            self.__name = name
            self.__gender = gender

    def __repr__(self):
        return """
Person: {}
Gender: {}""".format(self.__gender, self.__name)

totally_not_francis = Person("Frank", "M")
totally_not_francis.__name = "Francis"
print(totally_not_francis.__name)
print(totally_not_francis)
print(totally_not_francis.__dict__)
totally_not_francis.__dict__["_Person__name"] = "Francis"
print(totally_not_francis)
