text = input('Enter the text: ').split()
i = 0
counts = []
res = []

for t in text:
    counts.append(t.count('a') + t.count('A'))

topLen = max(counts)

while i < len(counts):
    if counts[i] == topLen:
        res.append(text[i])
    i += 1

print(res)


