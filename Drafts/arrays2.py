arr = [int(item) for item in input('Fill the first list: ').split()]

temporary = []
res = []
i = 0

while i + 1 < len(arr):
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        temporary.append(arr[i])
        i += 1
    temporary.append(arr[i])
    res.append(temporary)
    temporary = []
    i += 1

maxCell = 0
largestChain = []

for c in res:
    if len(c) > maxCell:
        maxCell = len(c)
        largestChain = c

print(res)

# while i + 1 < len(arr):
#     if arr[i] < arr[i + 1]:
#         temporary.append(arr[i])
#         i += 1
#         continue
#     temporary.append(arr[i])
#     res.append(temporary)
#     temporary = []
#     i += 1
