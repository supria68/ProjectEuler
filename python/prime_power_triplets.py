"""
EP - 87

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""

import math

def sieve(limit):
    #Use Sieve of Eratosthenes to find all primes below limit
    
    is_prime = [True]*limit
    prime = [2]

    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True

    for i in range(3, math.ceil(math.sqrt(limit)), 2):
        idx = i*2
        while idx < limit:
            is_prime[idx] = False
            idx += i

    for i in range(3, limit, 2):
        if is_prime[i]:
            prime.append(i)

    return prime
    
def compute(limit):
    # lets get the prime below 50 million
    prime = sieve(math.ceil(limit / 2)) 
    total = {0} # result to return
    
    # We need only prime square, prime cube, and prime fourth power
    for i in range(2,5): 
        temp = set() # takes care of repeated numbers if any
        for p in prime:
            q = p ** i
            if q > limit:
                break   
            for x in total:
                if x + q <= limit:
                    temp.add(x + q) # sum of a prime square, prime cube, and prime fourth power
        total = temp
    return total

print(len(compute(50000000)))
