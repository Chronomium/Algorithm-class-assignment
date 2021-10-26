def calc_weight_on_planet(weight, g=23.1):
    mass_e = weight / 9.8
    weight_o = mass_e * g
    return weight_o

w_e = calc_weight_on_planet(120,9.8)
w = calc_weight_on_planet(120)
w_j = calc_weight_on_planet(120,23.1)
print(w_e)
print(w)
print(w_j)