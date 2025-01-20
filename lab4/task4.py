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