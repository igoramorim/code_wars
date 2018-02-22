# Write Number in Expanded Form
# You will be given a number and you will need to return it as a string in Expanded Form. For example:
#
# expanded_form(12) # Should return '10 + 2'
# expanded_form(42) # Should return '40 + 2'
# expanded_form(70304) # Should return '70000 + 300 + 4'
#
# NOTE: All numbers will be whole numbers greater than 0.

# https://www.khanacademy.org/math/pre-algebra/pre-algebra-arith-prop/pre-algebra-place-value/v/place-value-3

def expanded_form(num):
    li = []
    n = 1
    num_str = str(num)
    for i in num_str[::-1]:
        li.append(str(int(i)*n))
        n = n*10

    li.reverse()
    # filter removes all the '0's in the list
    li = list(filter(lambda i: i != '0', li))
    return ' + '.join(li)
    # return '{} = {}'.format(num, ' + '.join(li))


print(expanded_form(12)) # Should return '10 + 2'
print(expanded_form(427)) # Should return '40 + 2'
print(expanded_form(70304)) # Should return '70000 + 300 + 4'
