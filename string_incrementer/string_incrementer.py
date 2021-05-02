# https://www.codewars.com/kata/54a91a4883a7de5d7800009c

# Your job is to write a function which increments a string, to create a new string.
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to the new string.

# Examples:
# foo      -> foo1
# foobar23 -> foobar24
# foo0042  -> foo0043
# foo9     -> foo10
# foo099   -> foo100
# ''       -> 1
# Attention: If the number has leading zeros the amount of digits should be considered.


import re

def increment_string(strng):
    if strng.strip() == '':
        return '1'
    m = re.search(r'\d+$', strng)
    if m is not None:
        digits = m.group()
        new_number = 'x'
        new_str = strng.split(digits)[0] + new_number # strng.split(m.group())[0]+str(int(m.group())+1)
        # print(strng, new_str)
        return new_str
    else:
        return strng+'1'



# print('foo', increment_string('foo'))
# print('foobar23', increment_string('foobar23'))
print('foo0042', increment_string('foo0042'))
# print('foo9', increment_string('foo9'))
print('foo099', increment_string('foo099'))
# print('', increment_string(''))
