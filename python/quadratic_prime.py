"""
EP - 27

Euler discovered the remarkable quadratic formula:

n^2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39. However, when n=40,40^2+40+41=40(40+1)+41 is divisible
by 41, and certainly when n=41,41^2+41+41 is clearly divisible by 41.

The incredible formula n^2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n^2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n=0.

"""

#Solution:

import math

def isprime(num):
    """
    Function to check if the number is prime
    """
    for i in range(2 , (num // 2) + 1):
        if num % i == 0:
            return False
    return True

def findMax(a,b):
    """
    function that returns the value of n which results in maximum number of primes for the quadratic
    equation
    """
    n = 2 #lets start from 2
    max_value = 0

    while (isprime(abs(n**2 + a*n + b))):
        if n > max_value:
            max_value = n
        n += 1
    return max_value

def compute():
    """
    1. let n = 0, then n^2+an+b ==> b. For b to be prime, it should be a positive odd number(exception 2)
    2. let n = 1, then n^2+an+b ==> a+b+1. Since b is positive odd, and we want the solution to be prime, so a must be odd!
    3. Find the quadratic eq that produces maximum number of primes
    4. find which a and b value will result in maximum number.
    5. return the product of a,b
    """
    maxN, maxA, maxB = 0,0,0

    current_max = 0

    for a in range(-999, 1000, 2): # odd numbers
        for b in range(3, 1000, 2): # odd positive
            current_max = findMax(a,b)
            if current_max > maxN:
                maxN = current_max
                maxA = a
                maxB = b
    return (maxA * maxB)

print("product of the coefficients a and b : {}".format(compute()))
