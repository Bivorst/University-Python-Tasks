import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, atan

def f1(x):
    if x < -5:
        return 1
    elif -5 <= x < 0:
        return -(3 / 5) * x - 2
    elif 0 <= x < 2:
        return -sqrt(4 - x**2) if 4 - x**2 >= 0 else None
    elif 2 <= x < 4:
        return x - 2
    elif 4 <= x < 8:
        return 2 + sqrt(4 - (x - 6)**2) if 4 - (x - 6)**2 >= 0 else None
    else:
        return 2

def f2(x, b=0):
    return atan(x) + b

def taylor_series(x, eps=0.001):
    y = 0
    n = 0
    an = x
    while abs(an) >= eps:
        y += an
        n += 1
        an = (-1)**(n) * x**(n + 2) / (n + 2) 
    return y

Xbeg = -1
Xend = 1
Dx = 0.05
b = float(input("Enter the value of b for the second function (e.g., 1): "))
eps = 0.001

x_vals = np.arange(Xbeg, Xend + Dx, Dx)

f1_vals = [f1(x) for x in x_vals]
taylor_vals = [taylor_series(x, eps) for x in x_vals]
f2_vals = [f2(x, b) for x in x_vals]

plt.figure(figsize=(10, 6))
plt.plot(x_vals, f1_vals, label="f(x) (Direct calculation)", color='blue', linewidth=2)
plt.plot(x_vals, taylor_vals, label="f(x) (Taylor series)", color='green', linestyle='--', linewidth=2)
plt.plot(x_vals, f2_vals, label="f2(x)", color='red', linewidth=2)
plt.title("Function Plots")
plt.xlabel("X")
plt.ylabel("Y")
plt.axhline(0, color='black',linewidth=0.5) 
plt.axvline(0, color='black',linewidth=0.5)  
plt.grid(True)
plt.legend()
plt.show()