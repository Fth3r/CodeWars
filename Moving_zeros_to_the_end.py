# solving the 5 kyu moving zeros to the end kata
def move_zeros(lst):
    r_count = 0
    for i in range(len(lst)):
        if lst[i] != 0: 
            lst[r_count], lst[i] = lst[i], lst[r_count]
            r_count += 1
    return lst
