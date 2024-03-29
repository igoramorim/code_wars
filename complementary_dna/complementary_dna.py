# https://www.codewars.com/kata/554e4a2f232cdd87d9000038

# Deoxyribonucleic acid (DNA) is a chemical found in the nucleus of cells and carries
# the "instructions" for the development and functioning of living organisms.
#
# If you want to know more http://en.wikipedia.org/wiki/DNA
#
# In DNA strings, symbols "A" and "T" are complements of each other, as "C" and "G".
# You have function with one side of the DNA (string, except for Haskell); you need
# to get the other complementary side. DNA strand is never empty or there is no DNA
# at all (again, except for Haskell).


import unittest


def DNA_strand(dna):
    pairs = {
            'A': 'T',
            'T': 'A',
            'G':'C',
            'C':'G'
    }
    new_dna = ''
    for symbol in dna:
        new_dna += pairs[symbol]

    return new_dna


class MyTest(unittest.TestCase):

    def test(self):
        self.assertEqual(DNA_strand('AAAA'), 'TTTT', 'String AAAA is')
        self.assertEqual(DNA_strand('ATTGC'), 'TAACG', 'String ATTGC is')
        self.assertEqual(DNA_strand('GTAT'), 'CATA', 'String GTAT is')


if __name__ == '__main__':
    unittest.main()
