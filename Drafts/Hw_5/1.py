arr = [
    [1, 2, 3, 4],
    [4, 8, 2, 1],
    [1, 3, 3, 9],
    [2, 1, 0, 2],
]

arr2 = [
    [2, 2, 4, 3],
    [9, 1, 1, 5],
    [6, 8, 1, 7],
    [2, 9, 9, 7],
]

res = []
i = 0
k = 0
miniRes = []

for item in arr:
    while k < len(arr[i]):
        miniRes.append(max(arr2[i]) * item[k])
        k += 1
    i += 1
    k = 0
    res.append(miniRes)
    miniRes = []

print(res)
