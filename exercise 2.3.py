print('Wind-Chill-Temperature')
ta = eval(input('Enter the temperature in Fahrenheit: '))

while not -58 < ta < 41:
    print('Temperature must be between -58F and 41F')
    ta = eval(input('Please re-enter the temperature in Fahrenheit: '))

v = eval(input('Enter the wind speed miles per hour: '))

while not v >= 2:
    print('Speed must be greater or equal to 2')
    v = eval(input('Please re-enter the wind speed miles per hour: '))

twc = 35.74 + (0.6215*ta) - (35.75*v**0.16) + (0.4275*ta*v**0.16)
print('The wind chill index is',twc)