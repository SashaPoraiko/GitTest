firstArr = [int(item) for item in input('Fill the first list: ').split()]
secondArr = [int(item) for item in input('Fill the second list: ').split()]

product = 1
summary = 0
res = []

for i in firstArr + secondArr:
    if i not in res:
        res.append(i)
        summary += i
        product *= i

print('The summary is:{0}, and the elements is:{1}'.format(summary, res))
