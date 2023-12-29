# 6 kyu kata
def unique_in_order(seq):
    l = list()
    if seq: l.append(seq[0])
    for x in range(len(seq)):
        if x == 0: continue
        if seq[x] != seq[x-1]:
            l.append(seq[x])
            
    return l
