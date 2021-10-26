## Number 3 Fn. Exercise

def num_atoms(g, ar=196.97):
    n = g / ar
    L = 6.022*(10**23)
    return n * L

Au = num_atoms(10)
C = num_atoms(10,12.001)
H = num_atoms(10,1.008)
print(Au)
print(C)
print(H)