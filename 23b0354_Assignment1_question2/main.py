'''
    Geometry (Complex and Polar)
'''
from math import *
from complex import Complex
from polar import Polar
# import the classes


def modulus(c: Complex) -> float:
    return sqrt(c.x**2+c.y**2)
    

def arg(c: Complex) -> float:
    if c.x == 0:
        return (c.y/abs(c.y))*pi/2
    return atan(c.y/c.x)


def abscissa(p: Polar) -> float:
    return p.r*cos(p.t)
    

def ordinate(p: Polar) -> float:
    return p.r*sin(p.t)
    

def distance(z1: Complex, z2: Complex) -> float:
    return modulus(z1-z2)
    

if __name__ == '__main__':

    # you can use this area of code to check all the functions manually
    # one example of using the functions has been shown
    # run this using "python3 main.py"
    a = Complex(1,2)
    b = Complex(2,2)
    z = a + b # uses the overloaded add
    print(z)
    print(modulus(z)) # you can call after you implement
    x = Polar(2,pi/3) # uses the overloaded power
    print(x ** 2)
    print(distance(a,b))
    print(arg(b))
