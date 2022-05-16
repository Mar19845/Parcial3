'''
Codigo obtenido de: https://github.com/alondrapereira/KaratsubaAlgorithm/blob/master/main.py
'''

import random

# Params:
#   x = first integer
#   y = second integer
#   base = base 10

def karatsuba(x, y, base=10):
    # Base case: If one of the two integers has only one digit, multiply them.
    str_x = str(x)
    str_y = str(y)
    if len(str_x) == 1 or len(str_y) == 1:
        return x * y
    else:
        # Sets n to the integer with the most digits.
        n = max(len(str_x), len(str_y))
        half_of_n = n // 2
        a = x // (base ** half_of_n)
        b = x % (base ** half_of_n)
        c = y // (base ** half_of_n)
        d = y % (base ** half_of_n)
        # Recursively computes ac and bd
        ac = karatsuba(a, c)
        bd = karatsuba(b, d)
        # Calculates ad + bc using the Gaussian Trick [(a+b)(c+d) - bd - ac = ad + bc)]
        ad_plus_bc = karatsuba(a + b, c + d) - bd - ac
        # Returns final result using (10ˆn/2)(ac) + (10ˆn/2)(ad + bc) + bd
        return ((base ** (half_of_n*2)) * ac) + ((base ** half_of_n) * ad_plus_bc) + bd
    
    

print(karatsuba(41,42))