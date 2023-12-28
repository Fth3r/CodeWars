# 6 kyu kata
def array_diff(a, b):
    for i in list(a):
        if i in b:
            a.pop(a.index(i))
            
    return a
