from math import *

def fun():
    x = float(input('Enter the value of x: '))
    if x < 0:
        y = (2 - (-3)) / (-10 - 0) * (x - (-10)) + 2
    elif 0 <= x <= 3:
        y = -sqrt(3**2 - x**2)
    elif 3 < x <= 6:
        y = sqrt(3**2-(x-6)**2)
    else:
        y = 3
    print("X={0:.2f} Y={1:.2f}".format(x, y))
    return fun()
fun()