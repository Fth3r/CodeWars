# solving the 4 kyu smallest possible sum kata
import numpy as np
solution = lambda a: np.gcd.reduce(np.array(a)) * len(a)
