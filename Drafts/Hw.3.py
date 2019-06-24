# a(a-n)*(a-2n)...(a-n*n)

n = int(input('Enter the n: '))
a = int(input('Enter the a: '))

i = 1
res = 0

while i <= n:
    res += a * (a - i * n)
    i += 1

print('The result is:{0}'.format(res))
