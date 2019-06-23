a = int(input('Enter first number: '))
b = int(input('Enter the second number: '))
c = int(input('Enter the third number: '))

#print('The greatest number is:{0}'.format(max(a, b, c)))

if a > b and a > c:
    print('The greatest number is', a)
elif b > c:
    print('The greatest number is', b)
else:
    print('The greatest number is', c)
