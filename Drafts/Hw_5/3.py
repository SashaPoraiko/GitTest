text = input('Enter the text: ').split()

res = []

for word in text:
    if len(word) % 2 == 0:
        res.append(word)
    else:
        middle = int(len(word) / 2)
        res.append(word[:middle] + word[middle + 1:])

print(res)
