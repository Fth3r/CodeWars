# solving the 6 kyu multiples of 3 or 5 kata
def solution(n):
    sol = 0
    for i in range(n):
        sol += i if i % 3 == 0 or i % 5 == 0 else 0
        
    return sol if n > 0 else 0
