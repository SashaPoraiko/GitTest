# a(a-n)*(a-2n)   ...(a-n*n)

n = int(input('Enter the n: '))
a = float(input('Enter the a: '))

i = 1
res = a

while i <= n:
    res *= (a - i * n)
    i += 1

print('The result is: {0}'.format(res))

