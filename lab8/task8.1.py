import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
from math import *

def fun():
    if x < 0:
        y = (2 - (-3)) / (-10 - 0) * (x - (-10)) + 2
    elif 0 <= x <= 3:
        y = -sqrt(3**2 - x**2) if 3**2 - x**2 >= 0 else None
    elif 3 < x <= 6:
        y = sqrt(3**2 - (x - 6)**2) if 3**2 - (x - 6)**2 >= 0 else None
    else:
        y = 3
    print("X={0:.2f} Y={1:.2f}".format(x, y))

fun()

def calculate_y(x):
    if x < 0:
        y = (2 - (-3)) / (-10 - 0) * (x - (-10)) + 2
    elif 0 <= x <= 3:
        y = -sqrt(3**2 - x**2) if 3**2 - x**2 >= 0 else None
    elif 3 < x <= 6:
        y = sqrt(3**2 - (x - 6)**2) if 3**2 - (x - 6)**2 >= 0 else None
    else:
        y = 3
    return y

x_values = np.linspace(-10, 6, 1000)
y_values = []

for x in x_values:
    try:
        y = calculate_y(x)
        y_values.append(y if y is not None else np.nan)
    except ValueError:
        y_values.append(np.nan)

plt.figure(figsize=(12, 6))
plt.plot(x_values, y_values, label="y=f(x)", color="black")
plt.axhline(0, color="black", linewidth=0.5, linestyle="--")
plt.axvline(0, color="black", linewidth=0.5, linestyle="--")
plt.title("Function Graph", fontsize=14)
plt.xlabel("x", fontsize=12)
plt.ylabel("y", fontsize=12)
plt.grid()
plt.legend()
plt.show()