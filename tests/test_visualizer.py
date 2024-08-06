import unittest
from src.visualizer import plot

class TestVisualizer(unittest.TestCase):
    def test_plot(self):
        paths_XYs = [[[0, 0], [1, 1], [2, 2]]]
        try:
            plot(paths_XYs)
        except Exception as e:
            self.fail(f"Visualizer failed with exception {e}")

if __name__ == '__main__':
    unittest.main()
