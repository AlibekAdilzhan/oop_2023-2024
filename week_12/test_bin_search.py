import unittest
from bin_search import binary_search

class TestSearch(unittest.TestCase):
    def setUp(self):
        self.arr = [1, 3, 3, 21, 35, 35, 81, 91, 92, 100]
        self.L = 0
        self.R = len(self.arr) - 1

    def test_1(self):
        x = 3
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, True)
    
    def test_start(self):
        x = self.arr[0]
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, True)

    def test_end(self):
        x = self.arr[-1]
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, True)

    def test_no_element_1(self):
        x = 0
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, False)

    def test_no_element_2(self):
        x = 40
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, False)

    def test_no_element_3(self):
        x = 120
        res = binary_search(self.arr, self.L, self.R, x)
        self.assertEqual(res, False)


if __name__ == "__main__":
    unittest.main()