# 4 kyu kata
def exp_sum(n):
    p = [1]+[0]*n
    for x in range(1, n+1):
        for i, j in enumerate(range(x, n+1)):
            p[j] += p[i]
    return p[n]
