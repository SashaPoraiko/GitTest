text = input('Enter the text: ').split()
aCount = []
counter = 0
i = 0
indexes = []
res = []
for t in text:
    for item in t:
        if item == 'a' or item == 'A':
            counter += 1
    aCount.append(counter)
    counter = 0

topLen = max(aCount)

while i < len(aCount):
    if aCount[i] == topLen:
        res.append(text[i])
    i += 1

print(res)
