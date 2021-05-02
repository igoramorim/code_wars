# https://www.codewars.com/kata/513e08acc600c94f01000001

# The rgb() method is incomplete. Complete the method so that passing in RGB decimal
# values will result in a hexadecimal representation being returned. The valid decimal
# values for RGB are 0 - 255. Any (r,g,b) argument values that fall out of that range
# should be rounded to the closest valid value.
#
# The following are examples of expected output values:
#
# rgb(255, 255, 255) # returns FFFFFF
# rgb(255, 255, 300) # returns FFFFFF
# rgb(0,0,0) # returns 000000
# rgb(148, 0, 211) # returns 9400D3


def rgb(r, g, b):
    # python 2
    # return '#%02x%02x%02x' % (max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255)))

    # The 02 part tells format() to use at least 2 digits and to use zeros to pad it to length, x means lower-case hexadecimal.
    # You can also use X to upper-case hexadecimal
    return '#{:02x}{:02x}{:02x}'.format(max(0, min(r, 255)), max(0, min(g, 255)), max(0, min(b, 255)))


print(rgb(255, 255, 300))
print(rgb(255, 255, 255))
print(rgb(0, 0, 0))
print(rgb(148, 0, 211))
print(rgb(1, 2, 3))
print(rgb(254,253,252))
print(rgb(-20,275,125))
