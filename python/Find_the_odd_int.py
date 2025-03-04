#solving the 6kyu find the odd int kata!

# This first block was my first submission before I realized I 
# way overthought everything
from collections import defaultdict

def find_it(seq):
    d = defaultdict(int)
    for n in seq: d[n] += 1
    
    return [k for k, v in d.items() if v % 2 != 0][0]

# So then I submitted this one
find_it = lambda seq: [x for x in seq if seq.count(x)%2!=0][0]