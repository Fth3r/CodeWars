# 6 kyu kata
def duplicate_count(text):
    res = {c:v for c in text.lower() for v in range(text.lower().count(c)+ 1)} 
    count = 0     
    for v in res.values():
        if v > 1:
            count += 1
        
    return count
