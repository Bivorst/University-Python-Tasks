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