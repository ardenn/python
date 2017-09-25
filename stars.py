def diamond(height):
    if height % 2 == 0:
        print("height must be an odd number!!")
    else:
        midHeight = int(height / 2) + 1
        constant = 2 * height + 1
        for line in range(1, height + 1):
            if line <= midHeight:
                for space in range(midHeight - line):
                    print(" ", end="")
                for star in range(2 * line - 1):
                    print("*", end="")
                print("")  # make a new line
            # after mid range spaces=height-line and stars=11-2(line)
            else:
                for space in range(line - midHeight):
                    print(" ", end="")
                for star in range(constant - 2 * line):
                    print("*", end="")
                print("")

# diamond(9)


def diamondEmpty(height):
    if height % 2 == 0:
        height -= 1
    else:
        midHeight = int(height / 2) + 1
        constant = 2 * height + 1
        for line in range(1, height + 1):
            if line <= midHeight:
                for space in range(midHeight - line):
                    print(" ", end="")
                lineheight = len(range(2 * line - 1))
                count = 1
                for star in range(2 * line - 1):
                    if count == 1 or count == lineheight:
                        print("*", end="")
                    else:
                        print(" ", end="")
                    count += 1
                print("")  # make a new line
            # after mid range spaces=height-line and stars=11-2(line)
            else:
                for space in range(line - midHeight):
                    print(" ", end="")
                lineheight = len(range(constant - 2 * line))
                count = 1
                for star in range(constant - 2 * line):
                    if count == 1 or count == lineheight:
                        print("*", end="")
                    else:
                        print(" ", end="")
                    count += 1
                print("")

diamondEmpty(17)

import math


def andrew_diamond(height):
    midpoint = math.ceil(height / 2)

    line = incr = 1
    while line > 0:
        for space in range(height - line):
            print(" ", end="")
        for star in range((2 * line) - 1):
            print("*", end="")
        print("")

        if(line == midpoint):
            incr *= -1
        line += incr

#print("Andrew's diamond:")
# andrew_diamond(11)
