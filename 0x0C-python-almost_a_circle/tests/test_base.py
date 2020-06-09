""" Base class testing """
from models.base import Base
import unittest


class Test(unittest.TestCase):
    """ Test """
    def test_noID(self):
        """ No id arg """
        self.assertEqual(Base().id, 1)

    def test_withID(self):
        """ With id arg """
        obj = Base(20)
        self.assertEqual(obj.id, 20)
        del(obj)


if __name__ == '__main__':
    unittest.main()
