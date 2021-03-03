import math

def f12(x):
    if (x < -54):
        return (((math.e)**x -71*(x**7))**4 + 62*(x**6))
    if (x < -42):
        return x**4 + 6*(x**2) + 1;
    return math.sin(math.tan(x) - 20*(x**2)) - x**6