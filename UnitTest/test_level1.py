import unittest
from calc import Calculator

class TestOperations(unittest.TestCase):

    def test_add(self):
        calc1 = Calculator(8,2)
        self.assertEqual( calc1.do_add(), 10, "Add is wrong")

if __name__ == '__main__':
    unittest.main()