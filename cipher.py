cipher = {
    "A": "Q",
    "E": "Z",
    "Q": "A",
    "Z": "E",
    "T": "M",
    "M": "T",
    "W": "N",
    "N": "W",
    "O": "R",
    "R": "O",
    "L": "S",
    "S": "L"}
inputt = "Nobody will ever guess what I'm saying"
output = "wrbrdy niss zvzo guzll nhqm i't lqyiwg"

inputtList = [i for i in inputt.upper()]

for ind, val in enumerate(inputtList):
    if val in cipher:
        inputtList[ind] = cipher[val]
finalOutput = "".join(inputtList)

print(finalOutput.lower())
print(finalOutput.lower() == output)
