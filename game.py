import random
import sys


def reTry():
    while True:
        print("Do you wish to play again? y[Yes] n[No]:")
        reply = input("Response: ")
        reply = reply.upper()
        if reply == "Y":
            gamePlay()
        elif reply == "N":
            print("Exiting...")
            sys.exit()
        else:
            print("Please enter a valid response y[Yes] n[No]:")
            continue


def gamePlay():
    myNum = random.choice(range(1, 21))
    print("Am thinking of a number between 1 and 20")
    print("Try to guess the number in 6 attempts")
    attempts = 1
    while attempts <= 6:
        value = input("Enter guess " + str(attempts) + "(or exit to exit) : ")
        if value == myNum:
            print("Congrats!,You guessed correctly in " + str(attempts) + " attempts")
            reTry()
        elif value > myNum:
            attempts += 1
            print("Your guess is higher than my number! Please try again")
            continue
        elif value == "exit":
            print("Exiting...")
            break
            sys.exit()
        elif value > 20 and value < 1:
            attempts += 1
            print("Please enter a value in the range [1-20]")
            continue
        else:
            attempts += 1
            print("Your guess is lower than my number! Please try again")
            continue
    else:
        print("You have failed in 6 attempts. My number is " + str(myNum))
        reTry()
gamePlay()
