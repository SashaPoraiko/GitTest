import math

print('Enter data ')

firstKatet = float(input('Enter first katet '))
secondKatet = float(input('Enter second katet '))

gipot = math.sqrt(firstKatet ** 2 + secondKatet ** 2)
plosha = (firstKatet * secondKatet) / 2

print(gipot, 'Gipotenuza: ')
print(plosha, 'Plosha: ')
