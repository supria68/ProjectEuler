"""

EP - 37

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

"""
import math

def isPrime(num):
    """
    Function to check if the number is prime
    """
    if num <= 3 and num > 1:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True


def isTruncatable(p):
    """
    Right to left: divide by 10 until you reach 1. if all quotients are prime
    then its right truncatable
    Left to right: same in reversed manner
    """

    div = 10
    while div < p:
        if (not(isPrime(p % div)) or not(isPrime(p % div | 0))):
            return False

        div *= 10
    return True

def compute():
    total, count = 0, 0
    i = 23 #let's start with two digit prime

    while count < 11: # we should find only 11 primes
        if isPrime(i) and isTruncatable(i):
            count += 1
            total += i
        i += 2

    return total

print(compute())
