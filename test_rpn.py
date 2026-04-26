import unittest
import rpn

class TestBasics(unittest.TestCase): 
    def test_add(self): 
        result = rpn.calculate("1 1 +")
        self.assertEqual(2, result)
        result = rpn.calculate("1 1 -")
        self.assertEqual(0, result)
        result = rpn.calculate("1 2 *")
        self.assertEqual(2, result) 
        result = rpn.calculate("3 3 ^")
        self.assertEqual(27, result)
