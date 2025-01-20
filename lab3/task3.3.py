from math import *

print("Enter Xbeg, Xend, Dx, and Epsilon")
xb = float(input("Xbeg="))
xe = float(input("Xend="))
dx = float(input("Dx="))
eps = float(input("Epsilon="))

if xb <= -1 or xe > 1 or xb >= xe:
    print("Error: X must be within -1 < X ≤ 1 and Xbeg < Xend")
    exit()

step = dx if xb < xe else -dx
print("+--------+--------+----+")
print("|   X    |   Y    | N  |")
print("+--------+--------+----+")
xt = xb
while (xt <= xe + 1e-10 and step > 0) or (xt >= xe - 1e-10 and step < 0):
    an = xt
    n = 1
    y = an

    while True:
        an = (-1) ** n * (xt ** (n + 1)) / (n + 1)
        y += an
        if abs(an) < eps:
            break
        n += 1

    print("|{0:7.2f} |{1:7.3f} |{2:4} |".format(xt, y, n))
    xt += step
print("+--------+--------+----+")