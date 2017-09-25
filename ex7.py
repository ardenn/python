new = []
old = "learN python THe hArd way".lower().split(" ")
print(old)
for word in old:
    letters = [i for i in word]
    letters[0] = letters[0].upper()
    newWord = "".join(letters)
    new.append(newWord)

for i in new:
    print(i, end=" ")
