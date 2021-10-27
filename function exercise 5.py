## Function Exercise 5

def convert_to_celcius(f):
    celcius = 5/9 * (f - 32)
    return celcius

def convert_to_kelvin(c):
    kelvin = c + 273.15
    return kelvin

def convert_temp():
    fahrenheit = eval(input("Enter a temperature in Fahrenheit: "))
    celcius = convert_to_celcius(fahrenheit)
    kelvin = convert_to_kelvin(celcius)
    print("The temperature in Fahrenheit is:",fahrenheit)
    print("The temperature in Celcius is:", celcius)
    print("The temperature in Kelvin is:", kelvin)

convert_temp()
