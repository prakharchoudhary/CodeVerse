def multiply(a, b):
    if a == 0 or b == 0:
        return 0
    if b == 1:
        return a
    if a < b:
        return multiply(b, a)
    return a + multiply(a, b-1)

import unittest

class Test(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(multiply(5, 0), 0)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(1, 5), 5)
        self.assertEqual(multiply(5, 1), 5)
        self.assertEqual(multiply(5, 5), 25)
        self.assertEqual(multiply(5, 6), 30)
        self.assertEqual(multiply(7, 5), 35)

if __name__ == '__main__':
    unittest.main()