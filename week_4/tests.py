import unittest

from geoma_objects import Rectangle


class TestGeoma(unittest.TestCase):
    def test_area(self):
        rect1 = Rectangle(3, 8)
        result = rect1.get_area()
        self.assertEqual(result, 24)

    def test_perimeter(self):
        rect1 = Rectangle(3, 8)
        result = rect1.get_perimeter()
        self.assertEqual(result, 22)

    def test_atr_a(self):
        rect1 = Rectangle(3, 8)
        result = rect1.get_a()
        self.assertEqual(result, 3)

    def test_atr_b(self):
        rect1 = Rectangle(3, 8)
        result = rect1.get_b()
        self.assertEqual(result, 8)

if __name__ == "__main__":
    unittest.main()