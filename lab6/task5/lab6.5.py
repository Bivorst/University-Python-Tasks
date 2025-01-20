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