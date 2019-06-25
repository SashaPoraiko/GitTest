data = input('Enter the sentence: ').split()
greatestNumber = 0

for w in data:
    if w.__len__() > greatestNumber:
        greatestNumber = w.__len__()

for w in data:
    if w.__len__() == greatestNumber:
        data.remove(w)

print(' '.join(data))
