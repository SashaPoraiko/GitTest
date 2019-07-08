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


for item in arr:
    res.append([max(arr2[i]) * item2 for item2 in item])
    i += 1

print(res)
