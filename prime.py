'''for num in range(36, 212):

    if all(num % n != 0 for n in range(2, num)):
        print(num)

    if any(num % n == 0 for n in range(2, num)):
        continue
    else:
        print(num)
'''


def primeNumbers(lowerLimit, upperLimit):
    for num in range(lowerLimit, upperLimit + 1):
        if all(num % n != 0 for n in range(2, num)):
            print(num)


primeNumbers(36, 211)
