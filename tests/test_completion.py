import unittest
import numpy as np
from src.completion import complete_curves

class TestCompletion(unittest.TestCase):
    def test_complete_curves(self):
        paths_XYs = [[[np.array([0, 0]), np.array([1, 1]), np.array([2, 0])]]]
        completed = complete_curves(paths_XYs)
        self.assertEqual(len(completed), 1)
        self.assertTrue(np.allclose(completed[0][-1], [0, 0]))

if __name__ == '__main__':
    unittest.main()
