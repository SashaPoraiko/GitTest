firstArr = [int(item) for item in input('Fill the first list: ').split()]
secondArr = [int(item) for item in input('Fill the second list: ').split()]
crossingArr = []

for i in firstArr:
    if i in secondArr and i not in crossingArr:
        crossingArr.append(i)

print('The sum is:{0}, and the greatest element is:{1}'.format(sum(crossingArr), max(crossingArr)))

