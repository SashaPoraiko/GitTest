data = input('Enter the sentence: ').split()
newData = []
i = 0

while i < data.__len__():
    if not newData.__contains__(data[i]):
        newData.append(data[i])
    i += 1

print(' '.join(newData))
