""" Rectangle testing """
from models.rectangle import Rectangle
import unittest


class Test(unittest.TestCase):
    """ Test """
    def test_allArgs(self):
        """ Doc tmp """
        obj = Rectangle(5, 10, 0, 0, 10)
        self.assertEqual(obj.width, 5)
        self.assertEqual(obj.height, 10)
        self.assertEqual(obj.id, 10)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)

    def test_widthTypeError(self):
        """ Doc tmp """
        with self.assertRaises(TypeError):
            obj = Rectangle("width", 10)

    def test_widthValueError(self):
        """ Doc tmp """
        with self.assertRaises(ValueError):
            obj = Rectangle(0, 10)

    def test_heightTypeError(self):
        """ Doc tmp """
        with self.assertRaises(TypeError):
            obj = Rectangle(10, "height")

    def test_heightValueError(self):
        """ Doc tmp """
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 0)

    def test_xTypeError(self):
        """ Doc tmp """
        with self.assertRaises(TypeError):
            obj = Rectangle(10, 10, "x")

    def test_xValueError(self):
        """ Doc tmp """
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 10, -5)

    def test_widthTypeError(self):
        """ Doc tmp """
        with self.assertRaises(TypeError):
            obj = Rectangle("width", 10)

    def test_yValueError(self):
        """ Doc tmp """
        with self.assertRaises(ValueError):
            obj = Rectangle(10, 10, 0, -5)

    def test_area(self):
        """ Doc tmp """
        self.assertEqual(Rectangle(5, 10).area(), 50)

    def test_str(self):
        """ Doc tmp """
        self.assertEqual(str(Rectangle(2, 4, 0, 0, 1)),
                         "[Rectangle] (1) 0/0 - 2/4")

if __name__ == "__main__":
    unittest.main()
