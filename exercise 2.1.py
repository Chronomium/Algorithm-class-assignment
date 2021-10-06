import math

print('Ramp Angle')

mass = eval(input('Enter the mass of the cart: '))
force = eval(input('Enter the force of the cart: '))
g = 9.8

count = format(math.degrees(math.asin(mass/(force*g))), '.1f')

print('The angle of the ramp is', count)