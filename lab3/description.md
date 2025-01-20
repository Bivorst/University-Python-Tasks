# Lab Work #3: Function Calculation and Integration via Series Expansion

## Objective:
This lab consists of three parts designed to practice calculations of graphical functions, verifying point inclusion within a defined area, and using series expansions to compute integrals.

## Part 3.1: Function Calculation from Graph

### Task Description:
Calculate and display (or save to a file) the values of a function defined graphically within an interval `[Xbeg, Xend]` with a step `dx`. The interval and step must be chosen to test all program branches. The table should include a title and a header.

### Graph Description:
The function is defined piecewise:
- For `x < 0`: A linear segment connecting points (-10, -3) and (0, 2).
- For `0 ≤ x ≤ 3`: A semicircle of radius 3 centered at (0, 0).
- For `3 < x ≤ 6`: A semicircle of radius 3 centered at (6, 0).
- For `x > 6`: A constant value of 3.

### Example Code:
```python
from math import *

print("Enter Xbeg, Xend, and Dx")
xb = float(input("Xbeg="))
xe = float(input("Xend="))
dx = float(input("Dx="))

if xb > xe and dx > 0:
    dx = -dx

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("Dx={0: 7.2f}".format(dx))
print("+-------+-------+")
print("|   X   |   Y   |")
print("+-------+-------+")
xt = xb
while (dx > 0 and xt <= xe) or (dx < 0 and xt >= xe):
    if xt < 0:
        y = (2 - (-3)) / (-10 - 0) * (xt - (-10)) + 2
    elif 0 <= xt <= 3:
        y = -sqrt(3**2 - xt**2)
    elif 3 < xt <= 6:
        y = sqrt(3**2 - (xt - 6)**2)
    else:
        y = 3
    if y is not None:
        print("|{0: 7.2f} |{1: 7.2f} |".format(xt, y))
    else:
        print("|{0: 7.2f} |   N/A  |".format(xt))
    xt += dx
print("+-------+-------+")
```

### How It Works:
- The program prompts the user for the interval and step size.
- Based on the value of `x`, the program computes `y` using the corresponding segment of the piecewise function.
- The results are displayed as a table with appropriate formatting.

## Part 3.2: Point Inclusion in a Shaded Area

### Task Description:
For ten randomly generated points, determine if they fall inside a shaded area consisting of a semicircle and a triangle. Display the results as text messages.

### Graph Description:
The shaded area includes:
- A semicircle with radius 1 centered at (0, 0) for `x ∈ [-1, 1]` and `y ≥ 0`.
- A triangle with vertices at (-1, -1), (0, 0), and (0, -1).

### Example Code:
```python
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
```

### How It Works:
- Random coordinates are generated for ten points.
- A function checks whether each point lies inside the shaded region by evaluating conditions for the semicircle and triangle.
- Results are displayed in a formatted table.

## Part 3.3: Series Expansion for Integral Calculation

### Task Description:
Calculate and display values of the natural logarithm function using its series expansion, with a user-defined interval `[Xbeg, Xend]`, step `dx`, and accuracy `ε`. Display the number of terms summed for each result.

### Formula:
The natural logarithm is approximated as:
\[
\ln(x+1) = \sum_{n=0}^{\infty} \frac{(-1)^n x^{n+1}}{n+1}, \quad -1 < x \leq 1
\]

### Example Code:
```python
from math import *

print("Enter Xbeg, Xend, Dx, and Epsilon")
xb = float(input("Xbeg="))
xe = float(input("Xend="))
dx = float(input("Dx="))
eps = float(input("Epsilon="))

if xb <= -1 or xe > 1 or xb >= xe:
    print("Error: X must be within -1 < X ≤ 1 and Xbeg < Xend")
    exit()

step = dx if xb < xe else -dx
print("+--------+--------+----+")
print("|   X    |   Y    | N  |")
print("+--------+--------+----+")
xt = xb
while (xt <= xe + 1e-10 and step > 0) or (xt >= xe - 1e-10 and step < 0):
    an = xt
    n = 1
    y = an

    while True:
        an = (-1) ** n * (xt ** (n + 1)) / (n + 1)
        y += an
        if abs(an) < eps:
            break
        n += 1

    print("|{0:7.2f} |{1:7.3f} |{2:4} |".format(xt, y, n))
    xt += step
print("+--------+--------+----+")
```

### How It Works:
- The series expansion is computed for values in the specified range.
- Terms are added until the absolute value of the current term is less than `ε`.
- Results include the value of `x`, the calculated `ln(x+1)`, and the number of terms used.
