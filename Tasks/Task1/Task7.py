import math


inside_R = 10
inp = float(input('Enter the outside Radius: '))
if inp > inside_R:
    outside_R = inp
inside_D = inside_R * 2
outside_D = outside_R * 2
resultSquare = 0.07 * (outside_D ** 2 - inside_D ** 2)
print('The resul is: ', resultSquare)
