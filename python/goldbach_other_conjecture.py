"""
EP - 46

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""
import math

def isPrime(n):
    """
    Check if the number is prime
    """
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(n ** 0.5 + 1), 2):
        if n % i == 0:
            return False
    return True

def compute():
    """
    number = prime + 2 * some_num^2
    some_num = sqrt((number - prime) / 2) for the conjucture to be true.
    If this doesn't hold good then we have our result!

    """
    num = 9 # start with the first odd composite number
    primes = [2, 3, 5, 7]

    while True:
        if isPrime(num):
            primes.append(num)
        else:
            for i in primes:
                if math.sqrt((num - i) / 2) == int(math.sqrt((num - i) / 2)):
                    break # follows goldbach conjucture!
            else:
                return num # we got our number that doesnt follow goldbach conjucture
        num += 2
    
print(compute())
