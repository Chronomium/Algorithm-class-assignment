print("Konnichiwa")
edge1 = eval(input("Enter the first edge: "))
edge2 = eval(input("Enter the second edge: "))
edge3 = eval(input("Enter the third edge: "))

if edge1 + edge2 > edge3 and edge2 + edge3 > edge1 and edge1 + edge3 > edge2:
    perim = edge1 + edge2 + edge3
    print("Valid, the perimeter is",perim)
else:
    print("Invalid, the perimeter can't be calculated")