#!/usr/bin/env python
# module FIND_ROOTS
import numpy as np

def get_roots(a, b, c):
    roots = np.roots((a, b, c))
    return np.unique(roots[np.isreal(roots)])

if __name__=="__main__":
    coeffs = (1, 1, 1)
    a, b, c = coeffs 
    polynomial = np.poly1d(coeffs)
    roots = get_roots(*coeffs)
    print(roots)
    print([np.abs(polynomial(r)) for r in roots])
