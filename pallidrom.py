"""
A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward, such as madam or racecar. Sentence-length palindromes may be written when allowances are made for adjustments to capital letters, punctuation, and word dividers, such as "A man, a plan, a canal, Panama!", "Was it a car or a cat I saw?" or "No 'x' in Nixon".
"""

# check if text is palindrome


def checkPalindrome(value):
    text = value.lower().replace(" ", "")
    wordDict = {}
    oddGroups = []

    for letter in text:
        if letter in wordDict:
            wordDict[letter] += 1
        else:
            wordDict[letter] = 1

    for key in wordDict:
        if wordDict[key] % 2 != 0:
            oddGroups.append(key)

    if len(oddGroups) > 1:
        return False
    else:
        return True

print(checkPalindrome("abbcdbba"))
print(checkPalindrome("abcdef"))
print(checkPalindrome("Was it a car or a cat I saw"))
print(checkPalindrome("madam"))
print(checkPalindrome("madamc"))
