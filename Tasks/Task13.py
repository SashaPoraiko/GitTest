x = 1
num = 0
while num < 9:
    x = ((x + (x / 10)) * ((x + 1) + ((x + 1) / 10)))
    num += 1
    print(x)
#print(x)
