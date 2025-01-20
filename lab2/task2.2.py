import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def is_point_in_triangle(x, y):
    x1, y1 = -1, -1
    x2, y2 = 0, 0
    x3, y3 = 0, -1

    denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    if denominator == 0:
        return False

    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    c = 1 - a - b

    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def check_point(x, y):
    if (x >= -1 and x <= 1 and y >= 0 and x ** 2 + y ** 2 <= 1):
        return True
    if is_point_in_triangle(x, y):
        return True
    return False

x = float(input("Enter X: "))
y = float(input("Enter Y: "))

if check_point(x, y):
    print(f"The point ({x:.2f}, {y:.2f}) is inside the area.")
else:
    print(f"The point ({x:.2f}, {y:.2f}) is outside the area.")
