"""
Multiplication table for 4,5,9,11 running from 1 throught to 12
"""
#nums = [4, 5, 9, 11]
nums = [i for i in range(1, 11)]
for num in nums:
    for factor in range(1, 13):
        product = num * factor
        print("{}x{}={}".format(num, factor, str(product).zfill(2)).rjust(9), end=" ")
    print("\n", end="")
