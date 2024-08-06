import unittest
from src.reader import read_csv

class TestReader(unittest.TestCase):
    def test_read_csv(self):
        path_XYs = read_csv('data/examples/frag0.csv')
        self.assertIsNotNone(path_XYs)
        self.assertTrue(len(path_XYs) > 0)

if __name__ == '__main__':
    unittest.main()
