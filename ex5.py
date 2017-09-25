import sys
print(sys.version)
"""
num = 50
while num <= 130:
    if num % 2 == 0:
        print(num * 2)
    num += 1


All the prime numbers from 36 to 210
"""

for num2 in range(36, 212):
    for n in range(2, num2):
        if num2 % n == 0:
            break
    else:
        print(num2)
