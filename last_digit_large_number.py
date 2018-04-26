# Define a function
#
# def last_digit(n1, n2):
#   return
# that takes in two numbers a and b and returns the last decimal digit of a^b.
# Note that a and b may be very large!
#
# For example, the last decimal digit of 9^7 is 9, since 9^7 = 4782969. The last
# decimal digit of (2^200)^(2^300), which has over 10^92 decimal digits, is 6.
#
# The inputs to your function will always be non-negative integers.
#
# Examples
# last_digit(4, 1)                # returns 4
# last_digit(4, 2)                # returns 6
# last_digit(9, 7)                # returns 9
# last_digit(10, 10 ** 10)        # returns 0
# last_digit(2 ** 200, 2 ** 300)  # returns 6
#

# https://brilliant.org/wiki/finding-the-last-digit-of-a-power/


def last_digit(n1, n2):
    return pow(n1, n2, 10)


# Also a good solution:
#
# rules = {
#     0: [0,0,0,0],
#     1: [1,1,1,1],
#     2: [2,4,8,6],
#     3: [3,9,7,1],
#     4: [4,6,4,6],
#     5: [5,5,5,5],
#     6: [6,6,6,6],
#     7: [7,9,3,1],
#     8: [8,4,2,6],
#     9: [9,1,9,1],
# }
# def last_digit(n1, n2):
#     ruler = rules[int(str(n1)[-1])]
#     return 1 if n2 == 0 else ruler[(n2 % 4) - 1]
