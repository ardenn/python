import random


class StringHelper:

    @staticmethod
    def randomCase(string):
        tempstr = ""
        for char in string:
            tempstr += char.upper() if random.randint(0, 1) else char.lower()
        return tempstr

    @staticmethod
    def abbreviate(string, num):
        abb = string[:num]
        if len(string) > num:
            abb += "..."
        return abb

text = "Hello this is a test"
print(StringHelper.randomCase(text))
print(StringHelper.abbreviate("hello my name is", 5))
print(StringHelper.abbreviate("I am", 9))
