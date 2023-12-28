# 6 kyu kata
def find_uniq(arr):
    if arr[0] == arr[-1]:
        r = arr[0]
    else:
        r = arr [1]
        
    arr = set(arr)
    arr = list(arr)
    
    i = arr.index(r)
    if i == 0:
        return arr[1]
    else:
        return arr[0]
