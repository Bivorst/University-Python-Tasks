# Laboratory Work 8: Graphical Representation and Monte Carlo Method

## Overview
This laboratory work involves solving three tasks related to graphical representation using Python. The tasks focus on plotting functions, generating random points, and using the Monte Carlo method to estimate areas. We will use Python libraries like `matplotlib` and `numpy` to visualize and analyze the results.

## Task 8.1: Plotting a Piecewise Function
### Objective:
To solve the reverse task by plotting the graph of a given piecewise function over the interval from -10 to 6.

### Features:
- Plotting of a piecewise function with different segments.
- Handling of discontinuities in the function.
- Graphical visualization using `matplotlib`.

### Technologies Used:
- Python
- `matplotlib` (for plotting)
- `numpy` (for generating the range of x-values)

### Program Flow:
1. Define the function with multiple conditional segments.
2. Generate a range of x-values from -10 to 6.
3. Compute corresponding y-values using the defined function.
4. Plot the function and display the result using `matplotlib`.

### Example Code:
```python
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
```

## Task 8.2: Monte Carlo Method for Area Estimation
### Objective:
To generate a graphical representation of random points within a defined region (triangle and circle) and estimate the area of a shaded figure using the Monte Carlo method.

### Features:
- Random point generation inside a specified region.
- Estimation of the area using the Monte Carlo method.
- Graphical visualization of the region and points.

### Technologies Used:
- Python
- matplotlib (for plotting)
- numpy (for random number generation)

### Program Flow:
1. Define the region (triangle and circle).
2.	Generate random points within the region.
3.	Count the points that lie inside the region.
4.	Estimate the area by comparing the number of points inside the region to the total number of points.
5.	Display the result as a percentage and visualize the points using matplotlib.

### Example Code:
 ```python 
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
```

## Task 8.3: Plotting Multiple Functions
### Objective:
To plot two functions over an interval and compare the results. The first function is computed using the Taylor series, and the second is a user-defined function.

### Features:
- Plotting of the first function using the Taylor series.
- Plotting of the second function with a user-defined parameter.
- Comparison of the graphs.

### Technologies Used:
- Python
- matplotlib (for plotting)
- numpy (for numerical operations)

### Program Flow:
1.	Define the first function using the Taylor series expansion.
2.	Define the second function as a simple arctangent function.
3.	Compute the values for both functions over a defined interval.
4.	Plot both functions and compare the results.

### Example Code:
```python
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
```