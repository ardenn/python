words = {"the": "t-word", "and": "a-word", "cow": "c-word", "barn": "b-word"}
string = "The dogs and cows were at the barn"
expectedOutput = "t-word dogs a-word cows were at t-word b-word"
stringList = string.lower().split(" ")

for ind, val in enumerate(stringList):
    if val in words:
        stringList[ind] = words[val]
output = " ".join(stringList)

print(output)
print(output == expectedOutput)
