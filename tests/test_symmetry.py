import unittest
import numpy as np
from src.symmetry import find_symmetry

class TestSymmetry(unittest.TestCase):
    def test_find_symmetry(self):
        paths_XYs = [[[np.array([0, 0]), np.array([1, 0]), np.array([2, 0])]]]
        symmetric = find_symmetry(paths_XYs)
        self.assertEqual(len(symmetric), 1)
        self.assertTrue(np.allclose(symmetric[0], [[0, 0], [1, 0], [2, 0]]))

if __name__ == '__main__':
    unittest.main()
