from math import sqrt
from random import uniform

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

print("Shot Results:")
print("+--------+--------+--------------+")
print("|   X    |   Y    |   Result     |")
print("+--------+--------+--------------+")
for _ in range(10):
    x = round(uniform(-1, 4), 2)
    y = round(uniform(-1, 10), 2)
    result = "Hit" if check_point(x, y) else "Miss"
    print("| {0:6.2f} | {1:6.2f} | {2:12} |".format(x, y, result))
print("+--------+--------+--------------+")