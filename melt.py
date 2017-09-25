"""
for numbers in range 10 to 50
print melt if divisible by 3
water if by 5
meltwater if by 3 and 5
number if not by both
"""
for num in range(10, 51):
    if num % 3 == 0 and num % 5 == 0:
        print(str(num) + '\tmeltwater')
    elif num % 5 == 0:
        print(str(num) + '\twater')
    elif num % 3 == 0:
        print(str(num) + '\tmelt')
    else:
        print(str(num) + '\tnumber')
