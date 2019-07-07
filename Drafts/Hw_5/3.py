text = input('Enter the text: ').split()
newWord = ''
res = []
middle = 0
i = 0

for t in text:
    if len(t) % 2 != 0:
        middle = int(len(t) / 2)
        while i < len(t):
            if i == middle:
                i += 1
                continue
            newWord += t[i]
            i += 1
        i = 0
    res.append(newWord)
    newWord = ''

print(res)
