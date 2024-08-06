import unittest
import numpy as np
from src.regularizer import regularize_shapes

class TestRegularizer(unittest.TestCase):
    def test_regularize_shapes(self):
        paths_XYs = [[[np.array([0, 0]), np.array([1, 1]), np.array([2, 2])]]]
        regularized = regularize_shapes(paths_XYs)
        self.assertEqual(len(regularized), 1)
        self.assertTrue(np.allclose(regularized[0], [[0, 0], [2, 2]]))

if __name__ == '__main__':
    unittest.main()
