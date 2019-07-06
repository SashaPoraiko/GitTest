import math

arr = [
    [1, 2, 3, 4],
    [4, 8, 2, 1],
    [1, 3, 3, 9],
    [2, 1, 0, 2],
]

x = 2

b = 1
res = 0
n = len(arr)
k = 1
# b*x^(n-1)+b*x^(n-2)

for item in arr:
    for item2 in item:
        if item2 > 0:
            b = item2
            break
    res += b * math.pow(x, n - k)
    b = 1
    k += 1

print(res)
