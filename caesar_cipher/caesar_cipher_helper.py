# https://www.codewars.com/kata/526d42b6526963598d0004db

# Write a class that, when given a string, will return an uppercase string with each
# letter shifted forward in the alphabet by however many spots the cipher was initialized to.
#
# For example:
#
# c = CaesarCipher(5); # creates a CipherHelper with a shift of five
# c.encode('Codewars') # returns 'HTIJBFWX'
# c.decode('BFKKQJX') # returns 'WAFFLES'
#
# If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.

# ######################################################################
#
# ##################### A BETTER SOLUTION ##############################
#
# from string import maketrans
#
# class CaesarCipher(object):
#
#     def __init__(self, shift):
#         self.alpha = "abcdefghijklmnopqrstuvwxyz".upper()
#         self.newalpha = self.alpha[shift:] + self.alpha[:shift]
#
#
#     def encode(self, str):
#         # maketrans(in, out) returns a translation table that maps each character
#         # in the intabstring into the character at the same position in the outtab string.
#         # Then this table is passed to the translate() function.
#
#         t = maketrans(self.alpha, self.newalpha)
#         return str.upper().translate(t)
#
#
#     def decode(self, str):
#         t = maketrans(self.newalpha, self.alpha)
#         return str.upper().translate(t)
#
# ######################################################################

import string import ascii_uppercase

class CaesarCipher(object):
    def __init__(self, shift):
        self.shift = shift
        self.letters = ascii_uppercase
        self.new_letters = self.letters[self.shift:] + self.letters[:self.shift]
        self.dict_cipher = {}

        for i in range(len(self.letters)):
            self.dict_cipher[self.letters[i]] = self.new_letters[i]


    def encode(self, str):
        new_str = ''
        for s in str.upper():
            if s in self.dict_cipher:
                new_str += self.dict_cipher[s]
            else:
                new_str += s
        print(new_str)
        return new_str


    def decode(self, str):
        new_str = ''
        for s in str.upper():
            if s in self.dict_cipher:
                for key, value in self.dict_cipher.items():
                    if s == value:
                        new_str += key
            else:
                new_str += s
        print(new_str)
        return new_str


c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
