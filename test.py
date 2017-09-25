for line in range(2):
    for space in range(line + 1):
        print(" ", end="")
    for star in range((-2 * line) + 3):
        print("*", end="")
    print("")
