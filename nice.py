'''
def say_nice_things(noun, adjective):
    print("{} is {}!!!".format(noun, adjective))

for noun, adjective in [["Francis", "awesome"], [
        "Mest", "interesting"], ["A turtle", "turtle-ish"]]:
    say_nice_things(noun, adjective)


say_nice_things("Andrew", "wonderful")
say_nice_things("Rodgers", "one of a kind")


say_nice_things(adjective="in-charge", noun="Andrew")


def say_a_lot(*args):
    print("I like: ")
    for word in args:
        print("\t" + str(word))
    print("a lot")

say_a_lot("Cows", "Pigs", "MEST", 4)
'''


def add_all_nums(*nums):
    value = 0
    for num in nums:
        value += num
    print(value)

add_all_nums(72, 6, -3, 8, 1.5, 4)


def get_squares(*myNums):
    myList = []
    for num in myNums:
        myList.append(num**2)
    print(myList)

get_squares(1, 3, 9, 5)
get_squares(13, 25)
