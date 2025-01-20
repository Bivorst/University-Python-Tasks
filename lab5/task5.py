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