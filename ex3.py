# while loops
i = 14
while i >= -1:
    if i < 0:
        print("{} is negative".format(i))
    elif i % 2 == 0:
        print("{} is even".format(i))
    else:
        print("{} is odd".format(i))
    i -= 3
