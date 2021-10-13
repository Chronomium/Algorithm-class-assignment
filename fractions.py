import math
from fractions import Fraction

numerator = eval(input("Enter the numerator, value must be greater than 0: "))
while not numerator > 0:
    numerator = eval(input("Please re-enter the numerator, value must be greater than 0: "))

denominator = eval(input("Enter the denominator, value must be greater than 0: "))
while not denominator > 0:
    denominator = eval(input("Please re-enter the denominator, value must be greater than 0: "))

gcd = math.gcd(numerator,denominator)
mixed = numerator // denominator
mixedmod = numerator % denominator

if numerator > denominator:
    print(numerator,"/",denominator,"is an improper fraction.")
    if gcd != 1:
        print("This improper fraction can be reduced to",Fraction(numerator,denominator))
    else: print("This improper fraction cannot be reduced any further.")
    print("The mixed number is",mixed,"and",mixedmod,"/",denominator)
else: print(numerator,"/",denominator,"is a proper function.")
if gcd != 1:
    print("This proper fraction can be reduced to",Fraction(numerator,denominator))
else: print("This proper fraction cannot be reduced any further.")

