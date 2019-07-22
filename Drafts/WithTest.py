arr = []

with open('Numbers.txt', 'r') as myFile:
    for line in myFile:
        arr.append(int(line))

print(arr)
