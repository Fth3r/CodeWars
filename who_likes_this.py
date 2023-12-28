# 6 kyu kata
def likes(names):
    if len(names) == 0:
        p = "no one likes this"
        return p
    elif len(names) == 1:
        p = names[0] + " likes this"
        return p
    elif len(names) == 2:
        p = names[0] + " and " + names[1] + " like this"
        return p
    elif len(names) == 3:
        p = names[0] + ", " + names[1] + " and " + names[2] + " like this"
        return p
    elif len(names) > 3:
        p = names[0] + ", " + names[1] + " and " + str(len(names) - 2) + " others like this"
        return p
