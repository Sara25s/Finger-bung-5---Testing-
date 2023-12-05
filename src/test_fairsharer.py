import unittest
from fairsharer import fair_sharer

class TestFairSharerFunction(unittest.TestCase):

    def test_single_iteration(self):
        initial_values = [0, 1000, 800, 0]
        result = fair_sharer(initial_values, 1)
        self.assertEqual(result, [100, 800, 900, 0])

    def test_multiple_iterations(self):
        initial_values = [0, 1000, 800, 0]
        result = fair_sharer(initial_values, 2)
        self.assertEqual(result, [100, 890, 720, 90])

    # Add more test cases as needed...

if __name__ == '__main__':
    unittest.main()
