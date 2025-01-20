# Lab Work #5: Operations with a Square Matrix

## Objective:
- Perform operations on a square matrix to calculate:
  1. The product of elements in rows that contain no negative elements.
  2. The minimum among the sums of the elements of diagonals parallel to the secondary diagonal.

---

## Task Description:
1. **Calculate the product of elements in rows with no negative elements.**
   - If a row contains only non-negative elements, compute the product of all elements in the row.
   - If no such rows exist, the result should indicate that.

2. **Find the minimum sum of the elements of diagonals parallel to the secondary diagonal.**
   - For all diagonals parallel to the secondary diagonal, calculate the sum of their elements.
   - Identify the diagonal with the smallest sum.

---

## Example Code:
```python
import numpy as np

def MakeMatr(n, a, b):
    return np.random.uniform(a, b, size=(n, n))

def PrintMatr(Matr):
    for row in Matr:
        print(" ".join(f"{elem:7.3f}" for elem in row))
    print()

def ProductOfNonNegativeRows(Matr):
    products = [np.prod(row) for row in Matr if np.all(row >= 0)]
    return products or [0]

def MinSumOfDiagonals(Matr):
    n = Matr.shape[0]
    diagonal_sums = []
    for d in range(-n + 1, n):
        diagonal = [Matr[i, i + d] for i in range(n) if 0 <= i + d < n]
        if diagonal:
            diagonal_sums.append(sum(diagonal))
    return min(diagonal_sums) if diagonal_sums else None

if __name__ == "__main__":
    n = int(input("Enter the size of the square matrix (NxN): "))
    MyMatr = MakeMatr(n, -10, 10)

    print("Generated Matrix:")
    PrintMatr(MyMatr)

    non_negative_products = ProductOfNonNegativeRows(MyMatr)
    if non_negative_products == [0]:
        print("No rows contain only non-negative elements.")
    else:
        print("Products of elements in rows without negative elements:", non_negative_products)

    min_diagonal_sum = MinSumOfDiagonals(MyMatr)
    if min_diagonal_sum is not None:
        print("Minimum sum among diagonals parallel to the secondary diagonal:", min_diagonal_sum)
    else:
        print("No diagonals found.")
```
## How It Works:
1.	Matrix Initialization:
	- The matrix is initialized with random floating-point values in a specified range.
	- Dimensions are NxN, where N is provided by the user.
2.	Row Product Calculation:
	- Each row is checked for the presence of negative values.
	- If no negatives are found, the product of the row’s elements is computed and stored.
3.	Diagonal Sum Calculation:
	- Diagonals parallel to the secondary diagonal are identified.
	- The sum of each diagonal’s elements is calculated.
	- The minimum sum among these diagonals is returned.
4.	Output:
	- The matrix is printed for reference.
	- Results for each task are displayed in a readable format.