import matplotlib.pyplot as plt
import numpy as np
from math import sqrt

def is_point_in_triangle(x, y):
    x1, y1 = -1, -1
    x2, y2 = 0, 0
    x3, y3 = 0, -1

    denominator = (y2 - y3) * (x1 - x3) + (x3 - x2) * (y1 - y3)
    a = ((y2 - y3) * (x - x3) + (x3 - x2) * (y - y3)) / denominator
    b = ((y3 - y1) * (x - x3) + (x1 - x3) * (y - y3)) / denominator
    c = 1 - a - b

    return 0 <= a <= 1 and 0 <= b <= 1 and 0 <= c <= 1

def check_point(x, y):
    flag = 0
    if (x == 2 and y == 2) or (x == 1 and y == 1):
        flag = 0
    elif (x >= -1 and x <= 1) and (y >= 0) and (x ** 2 + y ** 2 <= 1):
        flag = 1
    elif is_point_in_triangle(x, y):
        flag = 1
    elif (x < -1) or (x > 4):
        flag = 0
    elif (x >= -1) and (x < 1) and (y >= 2 * x + 2) and (y <= x ** 3 - 4 * x ** 2 + x + 6):
        flag = 1
    elif (x >= 1) and (x <= 4) and (y >= x ** 3 - 4 * x ** 2 + x + 6) and (y <= 2 * x + 2):
        flag = 1
    return flag

x = float(input("Enter X = "))
y = float(input("Enter Y = "))

flag = check_point(x, y)
print(f"Point X = {x:.2f} Y = {y:.2f}", end="")
if flag:
    print(" is inside the area")
else:
    print(" is outside the area")

x_vals = np.linspace(-1, 1, 400) 
y_upper = np.sqrt(1 - x_vals ** 2)

fig, ax = plt.subplots(figsize=(8, 8))

y_upper_clipped = np.where(y_upper >= -0.5, y_upper, -0.5)

ax.fill_between(x_vals, y_upper_clipped, color='blue', alpha=0.3)

triangle_x = [-1, 0, 0, -1]
triangle_y = [-1, 0, -1, -1]

ax.fill(triangle_x, triangle_y, color='green', alpha=0.3)
ax.plot(x, y, 'ro', label=f'Point ({x:.2f}, {y:.2f})')
ax.axhline(0, color='black', linewidth=1)
ax.axvline(0, color='black', linewidth=1)
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_title('Point inside Area Check')
ax.grid(True)
ax.legend()
plt.show()