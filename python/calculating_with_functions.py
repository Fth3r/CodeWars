# 5 kyu kata
import operator

symbols = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv
}

def zero(operation=None): return ((both := operation) and symbols[both[0]](0, both[1]) if operation else 0)
def one(operation=None): return ((both := operation) and symbols[both[0]](1, both[1]) if operation else 1)
def two(operation=None): return ((both := operation) and symbols[both[0]](2, both[1]) if operation else 2)
def three(operation=None): return ((both := operation) and symbols[both[0]](3, both[1]) if operation else 3)
def four(operation=None): return ((both := operation) and symbols[both[0]](4, both[1]) if operation else 4)
def five(operation=None): return ((both := operation) and symbols[both[0]](5, both[1]) if operation else 5)
def six(operation=None): return ((both := operation) and symbols[both[0]](6, both[1]) if operation else 6)
def seven(operation=None): return ((both := operation) and symbols[both[0]](7, both[1]) if operation else 7)
def eight(operation=None): return ((both := operation) and symbols[both[0]](8, both[1]) if operation else 8)
def nine(operation=None): return ((both := operation) and symbols[both[0]](9, both[1]) if operation else 9)

def plus(num): return '+', num
def minus(num): return '-', num
def times(num): return '*', num
def divided_by(num): return '/', num
