data = input('Enter the sentence: ').split()
greatestNumber = 0

for w in data:
    if len(w) > greatestNumber:
        greatestNumber = w.__len__()

arr=[]
for w in data:
    if len(w) < greatestNumber:
        arr.append(w)

print(' '.join(arr))
