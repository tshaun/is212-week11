import unittest
from ex2_smelly import Circle, Rectangle, Triangle, Shape

'''class TestShape(unittest.TestCase):

    def test_calculate_area_circle(self):
        # Test for a circle with radius 5
        result = Shape().calculate_area('circle', radius=5)
        self.assertAlmostEqual(result, 78.5, places=2)

    def test_calculate_area_rectangle(self):
        # Test for a rectangle with length 4 and width 6
        result = Shape().calculate_area('rectangle', length=4, width=6)
        self.assertEqual(result, 24)

    def test_calculate_area_triangle(self):
        # Test for a triangle with base 10 and height 8
        result = Shape().calculate_area('triangle', base=10, height=8)
        self.assertEqual(result, 40)
'''

class TestShape(unittest.TestCase):

    def test_calculate_area_circle(self):
        circle = Circle()
        result = circle.calculate_area(radius=5)
        self.assertAlmostEqual(result, 78.5, places=2)

    def test_calculate_area_rectangle(self):
        rectangle = Rectangle()
        result = rectangle.calculate_area(length=4, width=6)
        self.assertEqual(result, 24)

    def test_calculate_area_triangle(self):
        triangle = Triangle()
        result = triangle.calculate_area(base=10, height=8)
        self.assertEqual(result, 40)

if __name__ == '__main__':
    unittest.main()
