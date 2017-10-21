# ATM PIN

"""
Step 1: check if string has 4 or 6 digits
Step 2 Check if string is a number
"""


def is_valid_pin(string):
    if len(string) == 4 or len(string) == 6:
        return string.isdigit()
    return False

"""
A palindrome has at most one odd-group of letters
Step 1 Create a list to store odd-group letters
Step 2 Count the number of occurrences of each character and store it in the list if the count is odd
Step 3 Check if the length of odd_groups in at most one
"""


def is_palindrome(string):
    odd_groups = []
    for letter in string:
        if letter not in odd_groups:
            if string.count(letter) % 2 == 1:
                odd_groups.append(letter)
    return len(odd_groups) <= 1

"""
Step 1 Create a list of vowels
Step 2 Loop through the string and replace occurrences of vowels with an empty string
"""


def remove_vowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    for letter in string:
        if letter.lower() in vowels:
            string = string.replace(letter, "")
    return string
