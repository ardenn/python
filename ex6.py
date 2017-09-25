'''
IS_BEAUTIFUL = False
name = "Tshepo"
if IS_BEAUTIFUL or name == "Andrew":
    print("hi, beautiful")
else:
    print("Sorry S.A")

# print numbers from 11 to 53 that are even and divisible by 3

for num in range(10, 54, 2):
    if num % 3 == 0:
        print("{} is even and divisible by 3".format(num))
'''
#
nums = [1, 2, 3, 4, 5, 6, 3, 5, 1, -232]
ind = 1
while ind < len(nums):
    print(nums[ind])
    ind += 2

'''
for i in range(1, len(nums), 2):
    print(nums[i])
'''
