text = 'qe qe arrow arrow a r s'.split()

myDictionary = {}

for word in text:
    if word not in myDictionary:
        myDictionary[word] = 1
    else:
        myDictionary[word] += 1

res = []
maxim = max(myDictionary.values())

for key, value in myDictionary.items():
    if value == maxim:
        res.append(key)

print(min(res))
