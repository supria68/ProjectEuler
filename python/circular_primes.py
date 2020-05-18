"""
EP - 35

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""
import math

def sieve(limit):
    # Use Sieve of Eratosthenes to find ll primes within limit
    primes = [True] * limit
    primes[0] = primes[1] = False
    for i in range(2, math.floor(math.sqrt(limit))):
        if primes[i]:
            for j in range(i*i, limit, i):
                primes[j] = False
    return primes

def compute():
    limit = 999999
    isprime = sieve(limit)
    count = 0
    for num in range(2, limit):
        num = str(num)
        # perform circuar shift and check if they are prime
        if all(isprime[int(num[i:]+num[:i])] for i in range(len(num))):
            count += 1
    return count      
  
if __name__ == "__main__":
    print(compute())
