# https://www.codewars.com/kata/5412509bd436bd33920011bc

# Usually when you buy something, you're asked whether your credit card number, phone
# number or answer to your most secret question is still correct. However, since someone
# could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.
#
# Your task is to write a function maskify, which changes all but the last four characters into '#'.
#
# maskify("4556364607935616") == "############5616"
# maskify(     "64607935616") ==      "#######5616"
# maskify(               "1") ==                "1"
# maskify(                "") ==                 ""
#
# # "What was the name of your first pet?"
# maskify("Skippy")                                   == "##ippy"
# maskify("Nananananananananananananananana Batman!") == "####################################man!"


# return masked string
def maskify(cc):
    # '#' * (len(cc)-4) replace all characters but the last four into '#'
    # and + cc[-4:] get the last 4 original characters
    if len(cc) > 4:
        return '#' * (len(cc)-4) + cc[-4:]
    else:
        return cc


print(maskify('4556364607935616'))
print(maskify('64607935616'))
print(maskify('1'))
print(maskify(''))
print(maskify('Skippy'))
print(maskify('Nananananananananananananananana Batman!'))
