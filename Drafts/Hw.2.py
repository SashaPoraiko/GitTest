count = int(input("Enter the count of numbers: "))
# 1/1+1/2+1/3+...

result = 0
i = 0

while i < count:
    i += 1
    result += 1 / i

print(result)
