# solving the 4 kyu so many permutations! kata
from itertools import permutations as p

def permutations(s):
    l =  list(set(p(s)))
    for i in range(len(l)):
        l[i] = ''.join(l[i])
    return l
