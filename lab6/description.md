# Laboratory Work №6: Adjusting Programs to Use File Input and Output

## Objective:
Refactor the programs developed for Laboratory Works №1, №4, and №5 to ensure input and output are handled via files. 

## Description:
Previously, input data was provided via the keyboard, and results were displayed on the screen. To enhance usability and automation:
- Input data is prepared in text files.
- Program results are written to separate text files for easier analysis and reuse.

---

## Tasks:

### 6.1 Adjustment to Laboratory Work №1
#### Description:
- Prepare a text file with input data.
- Read the data from the file.
- Write the results into an output file in a formatted table.

#### Example Code:
```python
from math import *

def process_lab1(input_file, output_file):
    with open(input_file, 'r', encoding='cp1251') as fi:
        lines = fi.readlines()

    with open(output_file, 'w', encoding='cp1251') as fo:
        fo.write("+===+===+===+===+\n")
        fo.write("I  A  I  X  I   F1   I   F2   I\n")
        fo.write("+===+===+===+===+\n")

        for line in lines[2:]:
            try:
                a, x = map(float, line.strip().split())
            except ValueError:
                continue

            terms = [sin(a), cos(a), tan(a)]
            if terms[1] - ((2 * terms[0]) * (terms[0] * 2)) != 0:
                numerator = ((2 * terms[1]) * (terms[0] * 2)) - terms[0]
                denominator = terms[1] - ((2 * terms[0]) * (terms[0] * 2))
                f1_result = numerator / denominator
            else:
                f1_result = 0

            f2_result = pow(2, log(3 - cos(pi / 4 + 2 * x), 3 + sin(x))) / (1 + tan(2 * x / pi) ** 2)

            fo.write(f"I {a:6.2f} I {x:6.2f} I {f1_result:6.4f} I {f2_result:6.4f} I\n")

        fo.write("+===+===+===+===+\n")
```
### 6.2 Adjustment to Laboratory Work №4
#### Description:
- Read an array from an input file.
- Perform the following operations:
- Sum elements with odd indices.
- Calculate the sum of elements between the first and last negative values.
- Compress the array by removing elements with absolute values ≤ 1 and filling the remaining space with zeros.
- Write the results to an output file.

#### Example Code:
```python
from random import randint

def process_lab4(input_file, output_file):
    with open(input_file, "r") as fi:
        n = int(fi.readline().strip())
        mas = list(map(int, fi.readline().strip().split()))

    sum_odd_indices = sum(mas[i] for i in range(1, len(mas), 2))

    first_negative, last_negative = -1, -1
    for i, val in enumerate(mas):
        if val < 0:
            if first_negative == -1:
                first_negative = i
            last_negative = i

    if first_negative != -1 and last_negative != -1 and first_negative != last_negative:
        sum_between_negatives = sum(mas[first_negative + 1:last_negative])
    else:
        sum_between_negatives = 0

    mas = [x for x in mas if abs(x) > 1]
    mas += [0] * (n - len(mas))
    sum_odd_indices_compressed = sum(mas[i] for i in range(1, len(mas), 2))

    with open(output_file, "w") as fo:
        fo.write(f"Final array after compression:\n{mas}\n")
        fo.write(f"Sum of elements with odd indices (original array): {sum_odd_indices}\n")
        fo.write(f"Sum of elements with odd indices (compressed array): {sum_odd_indices_compressed}\n")
        fo.write(f"Sum of elements between first and last negative values: {sum_between_negatives}\n")
```
### 6.3 Adjustment to Laboratory Work №5
#### Description:
- Generate a matrix using the random function.
- Save the matrix to a file.
- Read the matrix back and perform the following operations:
- Sum elements in rows without negative values.
- Find the minimum sum of absolute values of diagonals parallel to the secondary diagonal.
- Write the results to an output file.

#### Example Code:
```python
import numpy as np

def create_matrix(n, m):
    return np.random.randint(-10, 10, size=(n, m))

def sum_positive_rows(matrix):
    return sum(np.sum(row) for row in matrix if np.all(row >= 0))

def min_diagonal_sums(matrix):
    n = matrix.shape[0]
    min_sum = float('inf')
    for d in range(-n + 1, n):
        diag_sum = sum(abs(matrix[i][n - 1 - i + d]) for i in range(n) if 0 <= n - 1 - i + d < n)
        min_sum = min(min_sum, diag_sum)
    return min_sum

def process_lab5(matrix_file, results_file):
    matrix = create_matrix(5, 5)
    np.savetxt(matrix_file, matrix, fmt="%d")

    matrix_from_file = np.loadtxt(matrix_file, dtype=int)
    positive_row_sum = sum_positive_rows(matrix_from_file)
    min_diagonal_sum = min_diagonal_sums(matrix_from_file)

    with open(results_file, "w") as fo:
        fo.write(f"Matrix:\n{matrix_from_file}\n")
        fo.write(f"Sum of rows without negative elements: {positive_row_sum}\n")
        fo.write(f"Minimum sum of diagonals parallel to the secondary diagonal: {min_diagonal_sum}\n")
```
#### Input and Output:
1.	Input Files: Provide properly formatted input data for each task.
2.	Output Files: Review the program results in the specified output files.