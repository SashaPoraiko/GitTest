text = 'qe qe arrow arrow a r s'.split()

myDictionary = {}

for word in text:
    if word not in myDictionary:
        myDictionary[word] = 1
    else:
        myDictionary[word] += 1

res = []

for key, value in myDictionary.items():
    if value == max(myDictionary.values()):
        res.append(key)

print(min(res))
