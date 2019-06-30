arr = [int(item) for item in input('Fill the list: ').split()]

res = []

i = 0

while i < len(arr):
    if arr.count(arr[i]) > 1 and not arr[i] in res:
        res.append(arr[i])
    i += 1

print(res)
