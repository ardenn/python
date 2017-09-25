# for loops

fav_nums = [2, 6, 3, 18, 11]
for num in fav_nums:
    if num % 2 == 0:
        print("{} is even".format(num))
        #print(str(num)+" is even")
    else:
        print("{} is odd".format(num))
