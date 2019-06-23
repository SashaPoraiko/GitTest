count = int(input("Enter the count of numbers: "))

x = 2
summary = 0
while count >= 0:
    count -= 1
    if summary != 0:
        summary += summary / (x + 1)
    else:
        summary += x / (x + 1)
    x += 1
print('The answer is:{0}'.format(summary))
