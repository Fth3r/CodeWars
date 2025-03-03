# Solving the 4 kyu kata Next bigger number with the same digits!

def next_bigger(n):
    if n / 10 < 1:
        return -1
    strn = str(n)
    for i in range(len(strn) - 1, -1, -1):
        if i == len(strn) - 1:
            continue
        if int(strn[i]) < int(strn[i + 1]):
            pivot, index = strn[i], i
            break
        elif i == 0:
            return -1

    it = 1
    for _ in range(int(max(strn[index:]))):
        for k in range(len(strn) - 1, index - 1, -1):
            if int(strn[k]) == int(pivot) + it:
                l = [x for x in strn]
                l[index], l[k] = l[k], l[index]
                return int(''.join(l[:index+1]) + ''.join(sorted(l[index+1:])))
        it += 1
    
# Above is my solution to the kata. Below are some of the more interesting solutions from 
# this challenge that I saw. I am saving them here so I can pick them apart later on. 

# By HMikiHTH
from itertools import permutations

def next_bigger(n):
    n = str(n)
    b = ''
    if len(n)>8:
        b = n[:-5]
        n = n[-5:]
    c = sorted({*map(''.join,permutations([*n],len(n)))})
    p = c.index(n)+1
    return -1 if p==len(c) else int(b+c[p])

# By RGeex
def next_bigger(n: int) -> int:
    s = str(n)[::-1]
    for i, x in enumerate(s):
        a, b = '0123456789'[int(x) + 1:], s[:i]
        m = min(set(a) & set(b), default='0')
        if x < m:
            return int(''.join([*sorted(s[:i+1].replace(m, '', 1))[::-1], m, s[i+1:]])[::-1])
    return -1