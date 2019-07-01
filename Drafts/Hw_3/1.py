arr = [int(item) for item in input('Fill the list: ').split()]

res = []

i = 0

while i < len(arr):
    if arr.count(arr[i]) > 1 and not arr[i] in res:
        res.append(arr[i])
    i += 1

# print('\n'.join(str(item) for item in res if ))

j = 0
res2 = []
for i in res:
    if j < 2:
        res2.append(i)
    else:
        print(res2)
        j = 0
        res2 = []
        res2.append(i)
    j += 1
print(res2)
