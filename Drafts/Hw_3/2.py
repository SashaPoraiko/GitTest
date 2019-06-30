firstArr = [int(item) for item in input('Fill the first list: ').split()]
secondArr = [int(item) for item in input('Fill the second list: ').split()]

product = 1
summary = 0

for w in (firstArr + secondArr):
    product *= w
    summary += w

print('The summary is:{0}, and the elements is:{1}'.format(summary, (firstArr + secondArr)))
