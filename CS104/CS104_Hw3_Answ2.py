pi = 3.141592

def a1():
    r = int(input("Enter the radii of the cylinder: "))
    return pi * (r **2)

def a2():
    r = int(input("Enter the radii of the cylinder: "))
    h = int(input("Enter the height of the cylinder: "))
    return 2 * pi * r * h

def a3():
    return(2*a1() + a2())

a3()
