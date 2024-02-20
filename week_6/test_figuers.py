from cw3 import Rectangle, Circle

import unittest

class TestFigures(unittest.TestCase):
    def test_rect_area(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.area(), 12.0)

    def test_rect_a(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.get_a(), 3)
    
    def test_rect_b(self):
        rect = Rectangle(3, 4)
        self.assertEqual(rect.get_b(), 4)

    def test_circ_area(self):
        circ = Circle(5.0)
        self.assertAlmostEqual(circ.area(), 78.5375, 3, "ERROR IN ROUNDING")


if __name__ == "__main__":
    unittest.main()

