import string


intab = "12"
outab = "  "

tress = "rodgers12"
trantab = tress.maketrans(intab, outab)
print(tress.translate(trantab))
