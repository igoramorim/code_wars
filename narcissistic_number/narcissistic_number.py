# A Narcissistic Number is a number which is the sum of its own digits,
# each raised to the power of the number of digits.
#
# For example, take 153 (3 digits):
#
# 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
#
# and 1634 (4 digits):
#
#  1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634


import unittest


def narcissistic(value):
    total = 0
    for n in str(value):
        total += int(n)**len(str(value))

    return total == int(value)


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(narcissistic(7), True, '7 is narcissistic')
        self.assertEqual(narcissistic(371), True, '371 is narcissistic')
        self.assertEqual(narcissistic(122), False, '122 is not narcissistic')
        self.assertEqual(narcissistic(4887), False, '4887 is not narcissistic')


if __name__ == '__main__':
    unittest.main()
