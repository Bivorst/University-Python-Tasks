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

    if terms[1] - ((2 * terms[0]) * (terms[0] * 2)) != 0: 
        numerator = ((2 * terms[1]) * (terms[0] * 2)) - terms[0]
        denominator = terms[1] - ((2 * terms[0]) * (terms[0] * 2))
        z1 = numerator/denominator
    else:
        z1 = 0
        print('The value provided leads to an undefined result for z1 due to division by zero.')

    z2 = terms[2] * 3

    examples = [z1,z2]
    print(examples)
    return fun()

fun()
