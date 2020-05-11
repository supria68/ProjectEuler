"""
EP - 7

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

Solution:
    We can use the algorithm- Sieve of Eratosthenes to get the prime value
    More information on algorithm is in problem EP - 10

"""

import summation_primes2

if __name__ == "__main__":
    limit = 110000
    prime_list = list(summation_primes2.prime(limit))
    # indexing in python starts from 0.
    # 10001st prime is the number at 10000 location in list
    print("10001st prime number: {}".format(prime_list[10000]))
