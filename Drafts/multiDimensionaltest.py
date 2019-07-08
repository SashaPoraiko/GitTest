# arr = [
#     [1, 2, 3, 4],
#     [4, 8, 2, 1],
#     [1, 3, 3, 9],
#     [2, 1, 0, 2],
# ]

arr = [
    [1, 2, 3, 3],
    [2, 2, 2, 2],
    [5, 5, 5, 5],
    [7, 7, 7, 7]

]


x = 3

i = 0
while i < len(arr):
    if x in arr[i]:
        k = arr[i].index(x)
        for item in arr:
            item.pop(k)
        arr.pop(i)
    else:
        i += 1

print(arr)
