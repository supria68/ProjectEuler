"""
EP - 49

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

"""

import math

def isPrime(num):
    if num % 2 == 0 or num % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def compute():
    """
    Triplets: a, b, c must be prime and permutations of each other
    a = b - 3330 = c - 6660
    upper limit (4-digit) = 10000 - 6660 = 3340

    """

    for a in range(1489, 3340):
        b = a + 3330
        c = b + 3330
        # check permutations
        if sorted(set(str(a))) == sorted(set(str(b))) and sorted(set(str(a))) == sorted(set(str(c))):
            # check if one of them is prime
            if isPrime(a):
                result = (a * 10000 + b) * 10000 + c
    return result

if name == "__main__":
    print(compute())
