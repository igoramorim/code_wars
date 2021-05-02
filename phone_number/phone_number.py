# https://www.codewars.com/kata/525f50e3b73515a6db000b83

# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in the form of a phone number.
#
# Example:
#
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
#
# The returned format must be correct in order to complete this challenge.
# Don't forget the space after the closing parenthesis!


import unittest


def create_phone_number(n):
    # convert the list of ints to a string
    s = ''.join(map(str, n))
    return '({pre}) {number1}-{number2}'.format(pre=''.join(s[:3]), number1=''.join(s[3:6]), number2=''.join(s[6:]))

    # smarter solution return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")
        self.assertEqual(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]), "(111) 111-1111")
        self.assertEqual(create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0]), "(023) 056-0890")
        self.assertEqual(create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]), "(000) 000-0000")


if __name__ == '__main__':
    unittest.main()
