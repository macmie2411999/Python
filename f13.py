import math

def f13(n,m):
    a = 0
    for i in range(1,n + 1):
        a += (math.cos(26*(i**2)) + (i**4)/68)

    b = 0
    for i in range(1,n + 1):
        for j in range(1,m + 1):
            b += (math.sin(j) + math.tan(i) - 52)
    return a - b