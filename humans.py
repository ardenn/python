input = "hd..h...d..h.d...h.h...d.h..h...d..hh..d.h"
inputt = [val for val in input]
print("".join(inputt))
length = len(inputt)
for pos in range(length):
    spacesAfterH = 1
    if inputt[pos] == "h" and pos < length - 1:
        while True:
            if inputt[pos + spacesAfterH] == "h":
                break
            elif inputt[pos + spacesAfterH] == "d" and spacesAfterH > 1:
                inputt[pos + 1] = "d"
                inputt[pos + spacesAfterH] = ''
                break
            else:
                spacesAfterH += 1
print("".join(inputt))
