arr = [int(item) for item in input('Fill the list: ').split()]

temporary = []
res = []
i = 0

while i + 1 < len(arr):
    while i + 1 < len(arr) and arr[i] < arr[i + 1]:
        temporary.append(arr[i])
        i += 1
    temporary.append(arr[i])
    if len(res) < len(temporary):
        res = temporary
    # res.append(temporary)
    temporary = []
    i += 1

# maxCell = 0
# largestChain = []
#
# for c in res:
#     if len(c) > maxCell:
#         maxCell = len(c)
#         largestChain = c

print(res)


