firstArr = [int(item) for item in input('Fill the first list: ').split()]
secondArr = [int(item) for item in input('Fill the second list: ').split()]
crossingArr = []

for item in firstArr:
    if item in secondArr and item not in crossingArr:
        crossingArr.append(item)

print('The sum is:{0}, and the greatest element is:{1}'.format(sum(crossingArr), max(crossingArr)))

