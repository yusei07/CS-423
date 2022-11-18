import math
import os

pi = math.pi

def cube():
    side = float(input("Enter the value of one side: "))
    vol = (side * side * side)
    sa = 6 * side * side
    print("Volume =", round(vol, 2)) 
    print("Surface area =", round(sa, 2))

def cuboid():
    w = float(input("Width: "))
    h = float(input("Height: "))
    l = float(input("Length: "))
    vol = (w * h * l)
    sa = 2 * ((l * h) * (w * h) * (l * w))
    print("Volume =", round(vol, 2)) 
    print("Surface area =", round(sa, 2))

def sphere():
    rad = float(input("Radius of sphere: "))
    sa = 4 * pi * rad **2
    vol = (4/3) * (pi * rad **3)
    print("Volume =", round(vol, 2)) 
    print("Surface area =", round(sa, 2))

def cylinder():
    h = float(input("Height: "))
    rad = float(input("Radius: "))
    vol = pi * rad * rad * h
    sa = ((2 * pi * rad) * h) + ((pi * rad **2)*2)
    print("Volume =", round(vol, 2)) 
    print("Surface area =", round(sa, 2))

def cone():
    h = float(input("Height: "))
    rad = float(input("Radius: "))
    slant_height = float(input("Slant height: "))
    vol = 1/3 * pi * rad * rad * h
    sa = pi * rad * slant_height + pi * rad * rad
    print("Volume =", round(vol, 2)) 
    print("Surface area =", round(sa, 2))

while True:
    menu = int(input("What do you wanna calculate?\n 1. Cube\n 2. Cuboid\n 3. Sphere\n 4. Cylinder\n 5. Cone\n\n 0. Exit program\n")) 
    os.system('clear')
    if(menu == 1):
        cube()
    elif(menu == 2):
        cuboid()
    elif(menu == 3):
        sphere()
    elif(menu == 4):
        cylinder()
    elif(menu == 5):
        cone()
    else: 
        break
