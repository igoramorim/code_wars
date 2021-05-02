# https://www.codewars.com/kata/52e1476c8147a7547a000811

# You need to write regex that will validate a password to make sure it meets the following criteria:
#
# At least six characters long
# contains a lowercase letter
# contains an uppercase letter
# contains a number
#
# Valid passwords will only be alphanumeric characters.

# From the docs:
#
# The solution is to use Python’s raw string notation for regular expression patterns;
# backslashes are not handled in any special way in a string literal prefixed with 'r'. So r"\n" is a
# two-character string containing '\' and 'n', while "\n" is a one-character string containing a newline.
# Usually patterns will be expressed in Python code using this raw string notation.
#
# [] Used to indicate a set of characters. Characters can be listed individually, or a range of characters
# can be indicated by giving two characters and separating them by a '-'. Special characters are not active
# inside sets. For example, [akm$] will match any of the characters 'a', 'k', 'm', or '$'; [a-z] will match
# any lowercase letter, and [a-zA-Z0-9] matches any letter or digit. Character classes such as \w or \S (defined below)
# are also acceptable inside a range, although the characters they match depends on whether ASCII or LOCALE mode is in force.
# If you want to include a ']' or a '-' inside a set, precede it with a backslash, or place it as the first character.
# The pattern []] will match ']', for example.
#
# {m,n} Causes the resulting RE to match from m to n repetitions of the preceding RE, attempting to match as many
# repetitions as possible. For example, a{3,5} will match from 3 to 5 'a' characters. Omitting m specifies a lower
# bound of zero, and omitting n specifies an infinite upper bound. As an example, a{4,}b will match aaaab or a thousand
# 'a' characters followed by a b, but not aaab. The comma may not be omitted or the modifier would be confused with the
# previously described form.


import re

# (?=.*) makes the class [] a requirement
# ^ start the word
# $ end the word
regex = '^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[a-zA-Z\d]{6,}$'

password = input('Type: ')

if re.search(regex, password):
    print('ok')
else:
    print('not ok')
