import math

gipot = float(input('Enter the value of gipotenuza '))
firstKatet = float(input('Enter the valueof firstKatet '))
secondKatet = math.sqrt(gipot ** 2 - firstKatet ** 2)
r = gipot / 2

print('The secondKatet is: ', secondKatet)
print('The circle square is: ', math.pi * r ** 2)
