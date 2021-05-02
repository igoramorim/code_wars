# https://www.codewars.com/kata/5262119038c0985a5b00029f

# Define a function isPrime/is_prime() that takes one integer argument and returns
# true/True or false/False depending on if the integer is a prime.
#
# Per Wikipedia, a prime number (or a prime) is a natural number greater than 1
# that has no positive divisors other than 1 and itself.
#
# Example
# isPrime(5)
# => true
#
# Assumptions
# You can assume you will be given an integer input.
# You can not assume that the integer will be only positive. You may be given
# negative numbers as well (or 0).


def is_prime(num):
    # prime numbers are greater than 1
    if num > 1:
        for i in range(2, num):
            if num%i == 0:
                return False
        else:
            return True
    else:
        return False


print(is_prime(5))
