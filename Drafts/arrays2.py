arr = [int(item) for item in input('Fill the first list: ').split()]

res = []
res2 = []
j = 1

while j < len(arr):
    if arr[j] > arr[j - 1]:
        res.append(arr[j - 1])
        res.append(arr[j])
    else:
        res2.append(res)
        res = []
    j += 1

maxlen = 0
maximum = []
k = 0

while k < len(res2):
    if len(res2[k]) > maxlen:
        maximum = res2[k]
        maxlen = len(res2[k])
    k += 1

print(res2)
