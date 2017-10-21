def normalWildCard(levels, char):
    nums = 1
    centerLength = (1 + (levels - 1) * 2)
    for level in range(levels):
        print(str(char * nums).center(centerLength))
        nums += 2

#normalWildCard(6, "B")


def inverseWildCard(levels, char):
    # centerLength = (1 + (levels - 1) * 2)
    nums = (1 + (levels - 1) * 2)
    for level in range(levels):
        print(str(char * nums).center(1 + (levels - 1) * 2))
        nums -= 2

#inverseWildCard(6, "*")


def treeStem(height, width, char, levels):
    centerLength = (1 + (levels - 1) * 2)
    for h in range(height):
        print(str(char * width).center(centerLength))

#treeStem(5, 3, "*", 9)


def printWildCard(levels, char):
    centerLength = (1 + (levels - 1) * 2)
    normalWildCard(levels, char)
    inverseWildCard(levels, char)

printWildCard(10, "*")
