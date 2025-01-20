# Lab Work #2: Function Calculation from Graph & Point Inclusion in a Shaded Area

## Objective:
1. Develop a Python program to calculate the value of a function based on a given argument, where the function is defined by a graph.
2. Write a Python program that determines whether a point with given coordinates falls within a shaded area. Points on the boundary are considered to belong to the area.

---

## Part ##2.1: Function Calculation from Graph
### Task Description:
1. The program computes the value of \( y \) based on the input \( x \), following the rules derived from the graph.
2. Handle different segments of the graph using conditional logic.
3. Display the result in a formatted output.

---

### Graph Description:
- For \( x < 0 \): The function is a linear segment from \( (-10, 2) \) to \( (0, -3) \).
- For \( 0 \leq x \leq 3 \): The function is a semicircle below the x-axis with a radius of 3 centered at \( (0, 0) \).
- For \( 3 < x \leq 6 \): The function is a semicircle above the x-axis with a radius of 3 centered at \( (6, 0) \).
- For \( x > 6 \): The function is constant at \( y = 3 \).

---

### Example Code:

```python
from math import sqrt

def fun():
    # Input the value of x
    x = float(input('Enter the value of x: '))
    
    # Compute the value of y based on the graph
    if x < 0:
        y = (2 - (-3)) / (-10 - 0) * (x - (-10)) + 2  # Linear segment
    elif 0 <= x <= 3:
        y = -sqrt(3**2 - x**2)  # Semicircle below the x-axis
    elif 3 < x <= 6:
        y = sqrt(3**2 - (x - 6)**2)  # Semicircle above the x-axis
    else:
        y = 3  # Constant segment
    
    # Display the result
    print("X = {0:.2f}, Y = {1:.2f}".format(x, y))
    return fun()

# Call the function
fun()
```

### How It Works:
1.	Input: The user enters a numeric value for ( x ).
2.	Processing:
	- The program evaluates ( x ) and determines the corresponding segment of the graph.
	- Based on the segment, it calculates ( y ) using appropriate mathematical operations:
	- Linear interpolation for ( x < 0 ).
	- Circle equation for ( 0 \leq x \leq 3 ) and ( 3 < x \leq 6 ).
	- A constant value for ( x > 6 ).
3.	Output: The result is displayed in the format ( X = {value}, Y = {value} ).
4.	Repeat: The program loops back to allow additional inputs.

## Part ##2.2: Point Inclusion in a Shaded Area

## Task Description:
1. Input the coordinates of the point (\( x \), \( y \)).
2. Check if the point falls within:
   - A semicircle of radius 1, centered at (0, 0), in the first quadrant.
   - A triangular region defined by the vertices \( (-1, -1) \), \( (0, 0) \), and \( (0, -1) \).
3. Output a message stating whether the point is inside or outside the shaded area.

---

## Graph Description:
- **Semicircle**: Covers the first quadrant with the equation \( x^2 + y^2 \leq 1 \) and \( y \geq 0 \).
- **Triangle**: Defined by the vertices \( (-1, -1) \), \( (0, 0) \), and \( (0, -1) \).

---

## Example Code:

```python
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
```

## How It Works:
1.	Input: The user enters the ( x ) and ( y ) coordinates of the point.
2.	Processing:
	- The program checks if the point is within the semicircle by evaluating the circle equation and ( y \geq 0 ).
	- For the triangle, it uses barycentric coordinates to determine inclusion.
3.	Output: Displays whether the point is inside or outside the shaded area.
4.	Loop/Expand: Can be integrated with graphical modules like matplotlib for visual representation.