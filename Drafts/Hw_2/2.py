data = input('Enter the sentence: ').split()
result = []
i = 0

while i < data.__len__():
    if not result.__contains__(data[i]):
        result.append(data[i])
    i += 1

print(' '.join(result))
