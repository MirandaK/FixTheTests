#!/usr/bin/env python
# module TEST_FINDS_ROOTS

import unittest
import random
import numpy as np

from find_roots import get_roots

def get_root_values():
    a = random.randint(0, 10)
    b = random.randint(0, 10)
    c = random.randint(0, 10)
    roots = get_roots(a, b, c)
    polynomial = np.poly1d((a, b, c))
    values = [polynomial(r) for r in roots]
    return values

class TestRoots(unittest.TestCase):
    def setUp(self):
        print('running TestRoots')

    def test_length_positive(self):
        roots = get_roots(a=1, b=0, c=-1)
        self.assertEqual(len(roots), 2)

    def test_length_negative(self):
        # TODO
        pass

    def test_length_edge(self):
        # TODO
        pass

    def test_zeros_positive(self):
        # TODO 
        pass

if __name__=="__main__":
    unittest.main()
