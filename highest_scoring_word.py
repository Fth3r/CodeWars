# 6 kyu kata
import string

def high(x):
    d = {k : 0 for k in x.split()}
    for w in d.keys():
        for l in w:
            index = string.ascii_lowercase.find(l)
            d[w] += index + 1
    
    val_lst = list(d.values())
    key_lst = list(d.keys())
    winner = 0
    
    for w in key_lst:
        index = list(d).index(w)
        if val_lst[index] > winner:
            winner = val_lst[index]
    pos = val_lst.index(winner)
    return (key_lst[pos])
