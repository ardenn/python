# multiplication table
for num in range(1, 11):
    for i in range(1, 11):
        val = num * i
        print(str("{}x{} = {}").format(num, i, str(val).zfill(2)).rjust(11), end="")
    print("")
