text = input('Enter the text: ').split()
newWord = ''
res = []
i = 0

for t in text:
    if len(t) % 2 == 0:
        res.append(t)
        continue
    else:
        while i < len(t):
            if i == int(len(t)/2):
                i += 1
                continue
            newWord += t[i]
            i += 1
        i = 0

    res.append(newWord)
    newWord = ''

print(res)
