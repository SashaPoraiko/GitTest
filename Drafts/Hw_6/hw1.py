
res = {}

while True:
    arr = input('Enter the data: ').split()
    if len(arr) != 2:
        break
    if arr[0] not in res:
        res[arr[0]] = int(arr[1])
    else:
        res[arr[0]] += int(arr[1])

for key, value in res.items():
    print('The {0} has reached {1} voices'.format(key, value))
