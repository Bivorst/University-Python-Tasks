from math import *

print("Enter Xbeg, Xend, and Dx")
xb = float(input("Xbeg="))
xe = float(input("Xend="))
dx = float(input("Dx="))

if xb > xe and dx > 0:
    dx = -dx

print("Xbeg={0: 7.2f} Xend={1: 7.2f}".format(xb, xe))
print("Dx={0: 7.2f}".format(dx))
print("+-------+-------+")
print("|   X   |   Y   |")
print("+-------+-------+")
xt = xb
while (dx > 0 and xt <= xe) or (dx < 0 and xt >= xe):
    if xt < 0:
        y = (2 - (-3)) / (-10 - 0) * (xt - (-10)) + 2
    elif 0 <= xt <= 3:
        y = -sqrt(3**2 - xt**2)
    elif 3 < xt <= 6:
        y = sqrt(3**2 - (xt - 6)**2)
    else:
        y = 3
    if y is not None:
        print("|{0: 7.2f} |{1: 7.2f} |".format(xt, y))
    else:
        print("|{0: 7.2f} |   N/A  |".format(xt))
    xt += dx
print("+-------+-------+")