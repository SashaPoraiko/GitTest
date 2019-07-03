arr = [
    [1, 2, 3, 4],
    [4, 8, 2, 1],
    [1, 3, 3, 9],
    [2, 1, 0, 2],
]
x = 3
res = []
indexer = -1
i = 0
k = 0

while i < len(arr):
    if x in arr[i]:
        k = 0
        while k < len(arr[i]) and arr[i][k] != x:
            k += 1
        print(k)
        for item in arr:
            item.pop(k)
        print(arr)
        arr.pop(i)
        print(arr)
    else:
        i += 1
