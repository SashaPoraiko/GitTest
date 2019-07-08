import math

arr = [
    [-1, -2, -3, -4],
    [-4, 8, 2, 1],
    [1, 3, 3, 9],
    [2, 1, 0, 2],
]

x = 2

res = 0
n = len(arr)
k = 1
# b*x^(n-1)+b*x^(n-2)

# for row in arr:
#     b = 1
#     for item in row:
#         if item > 0:
#             b = item
#             break
#     res += b * math.pow(x, n - k)
#     k += 1

for row in arr:
    i = 0
    length = len(row)
    while i < length and row[i] < 0:
        i += 1
    b = row[i] if i < length else 1
    res += b * math.pow(x, n - k)
    k += 1

print(res)
