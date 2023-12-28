# solving the 5 kyu Scramblies kata
from collections import Counter as c
def scramble(s1, s2):
    flag = 0
    counter = dict(c(s2))
    counter_again = dict(c(s1))
    for k,v in counter.items():
        if k in counter_again.keys() and v <= counter_again[k]:
            flag += 1
    return True if flag == len(counter) else False
    
# It ain't fancy, but it works!
