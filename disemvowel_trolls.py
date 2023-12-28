# 7 kyu kata
def disemvowel(string_):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for v in vowels:
        if v in string_:
            string_ = string_.replace(v, '')
            
    return string_
