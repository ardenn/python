import sys
print(sys.version)
# 1st problem - Print three lines
# L => Lines S => Spaces
# S = n - L
# stars = 2(line) - 1
'''
lines   spaces  stars
1       2       1
2       1       3
3       0       5
'''


def astericks(lines):
    # spaces = lines - line
    nums = 1
    for line in range(1, lines + 1):
        print(" " * (lines - line), end="")
        print("*" * nums)
        nums += 2

astericks(7)

'''
n = 3
for i in range(1, n + 1):
    print(i)
'''

for line in range(1, 6):
    for space in range(5 - line):
        print(" ", end="")
    for star in range(2 * line - 1):
        print("*", end="")
    print("")  # make a new line
