res = {}

while True:
    arr = input('Enter the data: ').split()
    if len(arr) != 2:
        break
    if arr[0] not in res:
        res[arr[0]] = int(arr[1])
    elif res[arr[0]] < int(arr[1]):
        res[arr[0]] = int(arr[1])

for key, value in res.items():
    print('The {0} player has {1} score'.format(key, value))
