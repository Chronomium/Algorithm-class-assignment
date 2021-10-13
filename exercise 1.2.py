speed = eval(input("Enter the plane's take off speed in m/s: "))
accel = eval(input("Enter the plane's acceleration in m/s: "))

length = (speed**2)/2*accel

print("The minimum runway length needed for this airplane is", length)