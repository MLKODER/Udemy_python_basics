age = 23

print("You are adult and you can buy alcohol") if age >= 18 else print('you are to young to buy alcohol')

isDrunk = False

print('You are adult and you can buy alcohol') if age >= 18 and not isDrunk else print('sorry, we cannot sell you alcohol')

isRestrictedArea = False

print('you can buy alcohol') if age >= 18 and not isDrunk and not isRestrictedArea else print('we cannot sell you alcohol')

#zadanie 1

min_likes = 500
min_shares = 100

num_of_likes = 1300
num_of_shares = 70

print('discount 10%') if num_of_likes >= min_likes and num_of_shares >= min_shares else print('not enough shares and likes')

#zadanie 2

isPizzaOrdered = True
isBigDrinkOrderes = False
isWeekend = False

print('free burger!!!') if not isWeekend and (isBigDrinkOrderes or isPizzaOrdered) else print('Buy pizza or big drink during work days to get free burger')

#zadanie 3

diskSize = 140
diskSizeUsed = 119
fileSize = 21

print('You can download file') if fileSize <= diskSize - diskSizeUsed else print('not enough space on disk')
