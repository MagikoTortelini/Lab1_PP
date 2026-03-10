import unittest

from program import Add

class CalculatorTest(unittest.TestCase):
    def test_blank(self):
        result = Add("");
        self.assertEqual(result,0)
    def test_return(self):
        result=Add("1")
        self.assertEqual(result,1)
    def test_add(self):
        result = Add("1,3")
        self.assertEqual(result,4)
    def test_multiple_numbers(self):
        result = Add("1,3,4")
        self.assertEqual(result,8)
    def test_valueerror(self):
        with self.assertRaises(ValueError):
            result=Add("1, 2")
    def test_newline(self):
        result = Add("1\n2,3")
        self.assertEqual(result, 6)
    def test_newline_2(self):
        with self.assertRaises(ValueError):
            result = Add("1\n,2")
    def test_endswith(self):
        with self.assertRaises(ValueError):
            result = Add("1,2,")





unittest.main(argv=['first-arg-is-ignored'],exit=False)