import math
a = int(input('Enter side a of triangle: '))
b = int(input('Enter side b of triangle: '))
c = int(input('Enter side c of triangle: '))

circ = a+b+c
s = circ/2

abcsq = math.sqrt(s*(s-a)*(s-b)*(s-c))

print(f'The circumference is {circ} and the area is {abcsq}')



