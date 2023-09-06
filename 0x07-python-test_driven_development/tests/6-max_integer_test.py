import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_single_element_list(self):
        self.assertEqual(max_integer([42]), 42)

    def test_positive_numbers(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([-1, 3, -2, 4]), 4)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()

