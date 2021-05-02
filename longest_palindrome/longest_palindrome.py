# https://www.codewars.com/kata/54bb6f887e5a80180900046b

# Find the length of the longest substring in the given string s that is the same in reverse.
#
# As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.
#
# If the length of the input string is 0, return value must be 0.
#
# Example:
# "a" -> 1
# "aab" -> 2
# "abcde" -> 1
# "zzbaabcd" -> 4
# "" -> 0


import unittest


def longest_palindrome(s):
    if s:
        longest = 0
        for start in range(len(s)):
            for end in range(len(s), start, -1):
                sub = s[start:end]
                if sub == sub[::-1]:
                    if len(sub) > longest:
                        longest = len(sub)

        return longest
    else:
        return 0


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(longest_palindrome("a"), 1)
        self.assertEqual(longest_palindrome("aa"), 2)
        self.assertEqual(longest_palindrome("baa"), 2)
        self.assertEqual(longest_palindrome("aab"), 2)
        self.assertEqual(longest_palindrome("abcdefghba"), 1)
        self.assertEqual(longest_palindrome("baablkj12345432133d"), 9)


if __name__ == '__main__':
    unittest.main()
