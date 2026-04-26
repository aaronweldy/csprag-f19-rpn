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

    def test_should_quit_accepts_common_exit_commands(self):
        self.assertTrue(rpn.should_quit("quit"))
        self.assertTrue(rpn.should_quit(" q "))
        self.assertTrue(rpn.should_quit("EXIT"))

    def test_should_quit_rejects_expression_input(self):
        self.assertFalse(rpn.should_quit("1 1 +"))
