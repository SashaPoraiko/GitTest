a = 1
b = 0.1
x = 1

while a < 10:
    x *= (a + b)
    a += 1
    b += 0.1
    print(x)
print(x)
