# Lab Work #1: Formula Calculations

## Objective:
Write a Python program to calculate the values of specific formulas. Prepare test cases in advance using a calculator or spreadsheet software like Excel. If some functions are missing in the language, derive them using existing functions.

---

## Task Description:
1. Implement a program to calculate the following formulas:
   - \( z_1 = \frac{2 \cos(a) \sin(2a) - \sin(a)}{\cos(a) - 2 \sin(a) \sin(2a)} \)
   - \( z_2 = \tan(3a) \)

2. Handle cases where the denominator of \( z_1 \) is zero and provide appropriate feedback.

3. Verify results with pre-computed values.

---

## Example Code:

```python
from math import sin, cos, tan

def fun(): 
    print("Enter an integer value for the variable.")
    while True:
        try:
            a = input('Input value: ')
            a = int(a)
        except ValueError:
            print("Invalid input. Please provide an integer value, e.g., 1, 2, 3.")
            return fun()
        break

    terms = [sin(a), cos(a), tan(a)]

    if terms[1] - (2 * terms[0] * terms[0] * 2) != 0: 
        numerator = (2 * terms[1] * terms[0] * 2) - terms[0]
        denominator = terms[1] - (2 * terms[0] * terms[0] * 2)
        z1 = numerator / denominator
    else:
        z1 = None
        print('The value provided leads to an undefined result for z1 due to division by zero.')

    z2 = terms[2] * 3

    results = [z1, z2]
    print(f"Results: z1 = {z1}, z2 = {z2}")
    return fun()

fun()
```

## How It Works:
1. The user inputs an integer value for ( a ).
2.	The program calculates the trigonometric terms ( \sin(a) ), ( \cos(a) ), and ( \tan(a) ).
3.	The program computes:
	- ( z_1 ) if the denominator is not zero.
	- ( z_2 = \tan(3a) ) as a scaled tangent function.
4.	The results are displayed. If the denominator in ( z_1 ) equals zero, the program provides a warning and sets ( z_1 ) to None.