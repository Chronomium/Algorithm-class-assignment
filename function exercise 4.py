## Function Exercise 4

def calc_new_height():
    c_width = eval(input("Enter the current width: "))
    c_height = eval(input("Enter the current height: "))
    new_width = eval(input("Enter the desired width: "))
    new_height = float((new_width * c_height) / c_width)
    print("The corresponding height is:",new_height)
    return new_height

new = calc_new_height()
print(new)