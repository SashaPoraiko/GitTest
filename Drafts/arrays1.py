# a<b
# arr=[item for item in ...]
a = float(input('Enter a: '))
b = float(input('Enter b: '))

# >=a<=b
summary = 0
product = 1
arr = []

x = [int(item) for item in input().split()]

print(x)

for item in x:
    if item < a:
        summary += item
    if item > b:
        product *= item
    if a <= item <= b:
        arr.append(item)

print(summary, product, max(arr), min(arr))
