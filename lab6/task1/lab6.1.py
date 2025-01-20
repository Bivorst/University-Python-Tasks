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