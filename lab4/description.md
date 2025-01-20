# Lab Work #4: Array Operations

## Objective:
Perform operations on a one-dimensional integer array, including calculating sums, compressing the array, and modifying its contents.

## Task Description:
1. Calculate the sum of elements at odd indices in the array.
2. Calculate the sum of elements located between the first and last negative elements in the array.
3. Compress the array by removing all elements whose absolute values are less than or equal to 1, filling the freed positions with zeros.

### Input:
- n: The number of elements in the array.
- The array is generated randomly with integer values ranging from -10 to 10.

### Output:
- The sum of elements at odd indices in the original array.
- The sum of elements between the first and last negative elements in the original array.
- The modified array after compression.
- The sum of elements at odd indices in the compressed array.

## Example Code:
```python
from random import randint

n = int(input("Number of elements in the array N: "))

mas = [randint(-10, 10) for _ in range(n)]

print("Initial array:")
print(mas)
sum_odd_indices = sum(mas[i] for i in range(1, len(mas), 2))
first_negative = -1
last_negative = -1
for i in range(n):
    if mas[i] < 0:
        if first_negative == -1:
            first_negative = i
        last_negative = i

if first_negative != -1 and last_negative != -1 and first_negative != last_negative:
    sum_between_negatives = sum(mas[i] for i in range(first_negative + 1, last_negative))
else:
    sum_between_negatives = 0

mas = [x for x in mas if abs(x) > 1]
mas += [0] * (n - len(mas))

print("\nFinal array after compression:")
print(mas)

sum_odd_indices_compressed = sum(mas[i] for i in range(1, len(mas), 2))

print("\nResults:")
print(f"Sum of elements at odd indices (original array): {sum_odd_indices}")
print(f"Sum of elements at odd indices (compressed array): {sum_odd_indices_compressed}")
print(f"Sum of elements between first and last negative elements: {sum_between_negatives}")
```

## How It Works:

1. Array Initialization:
    - The array is populated with random integers in the range [-10, 10].
2. Odd Index Sum Calculation:
    - The program iterates through odd indices of the array and calculates their sum.
3. Negative Elements:
    - The program identifies the indices of the first and last negative elements and calculates the sum of elements between them.
4. Array Compression:
    - Elements with an absolute value less than or equal to 1 are removed.
    - The remaining positions are filled with zeros to maintain the array's size.
5. Final Output:
    - The results of the calculations are displayed for both the original and compressed arrays.