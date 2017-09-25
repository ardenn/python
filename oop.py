# WaterBottle class
class WaterBottle:

    def __init__(self, color, shape, size, volume, owner):
        self.color = color
        self.shape = shape
        self.size = size
        self.volume = volume
        self.owner = owner

    def isMine(self):
        return self.owner == "rodgers"

    def isEmpty(self):
        return self.volume == 0

    def isUnique(self):
        return self.shape == "sphere"

    def changeVolume(self, newVol):
        self.volume = newVol
        return "The new Volume is: {}".format(self.volume)

    def __repr__(self):
        return """
		WaterBottle
		==================
		Shape: {}
		Size: {}
		Volume: {}
		Color: {}
		Owner: {}
        """.format(
            self.shape, self.size, self.volume, self.color, self.owner)

#bottle = WaterBottle("blue", "prism", "large", 50, "rodgers")

# print(bottle)
# print("\n")
# print("Empty: " + str(bottle.isEmpty()))
# print("\n")
# print("Unique: " + str(bottle.isUnique()))


class Teacher:

    def __init__(self, name, sub1, sub2):
        self.name = name
        self.sub1 = sub1[:]
        self.sub2 = sub2[:]

    def __str__(self):
        return """
		Successfully Added!
		Teacher:		{0}
		Subjects:
				{1}		Classes: {2}
				{3}		Classes: {4}
		""".format(self.name, self.sub1[0], ', '.join(self.sub1[1:]), self.sub2[0], ', '.join(self.sub2[1:]))

supergirl = Teacher(
    'Melissa Benoist', [
        'BIO', '1G', '2G', '3G', '4G'], [
            'CHEM', '1B', '2B', '3B', '4B'])
arrow = Teacher('Oliver Queen', ['CHEM', '1G', '2G', '3G', '4G'], ['BIO', '1B', '2B', '3B', '4B'])
print(supergirl)
print(arrow)
