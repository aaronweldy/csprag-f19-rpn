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

    def test_welcome_message_includes_joke(self):
        message = rpn.get_welcome_message()

        self.assertIn("Welcome to the RPN calculator!", message)
        self.assertIn("handle their operators", message)
