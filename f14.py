import math

def f14(x):
    if x == 0:
        return 7
    if x == 1:
        return 10
    else:
        return (math.sin(f14(x - 2)) + f14(x - 2)/33)

