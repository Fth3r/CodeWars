# solving for all integer solutions to the equation n = x^2-4y^2
from math import sqrt

def sol_equa(n):
    l = []
    for a in range(1, int(sqrt(n)+1)):
        b = n/a
        if b.is_integer():
            x = (a+b)/2
            y = (b-a)/4
            if x.is_integer() and y.is_integer(): l.append([x, y])
            
    return l
