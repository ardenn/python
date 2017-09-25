"""
print the words in the text with the number of occurences of each of the words
"""
#text = 'dogs come and eat and eat and eat'
text = 'The quick brown fox jumps over the lazy dog'
wordList = text.lower().split(" ")

wordDict = {}
for word in wordList:
    if word in wordDict:
        wordDict[word] += 1
    else:
        wordDict[word] = 1

print(wordDict)
