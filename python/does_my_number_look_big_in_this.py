# 6 kyu kata
def narcissistic( value ):
    n = 0
    
    for i in str(value):
        n += (int(i)**len(str(value)))
        
    return True if n == value else False
