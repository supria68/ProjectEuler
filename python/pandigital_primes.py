"""
EP - 41

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

# Solution:
    w.k.t,
    An integer is divisible by 3 if the sum of digits is divisible by 3. Such an integer is composite and not prime.
    
    9+8+7+6+5+4+3+2+1 = 45, 45/3 = 15
    8+7+6+5+4+3+2+1 = 36, 36/3 = 12
    7+6+5+4+3+2+1 = 28, 28/3 = 9.333…
    6+5+4+3+2+1 = 21, 21/3 = 7
    5+4+3+2+1 = 15, 15/3 = 5
    4+3+2+1 = 10, 4/3 = 1.333…
    3+2+1 = 6, 6/3 = 2
    2+1 = 3 3/3 = 1

    Only pandigital numbers of length 4 and 7 can form a prime number. The others cannot because any combination of their digits will sum to a number divisible by 3.

"""

import math,itertools as io

def isPrime(n):
    # check if the number is prime
    for i in range(2, math.ceil(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

def compute():
    p = io.permutations('1234567') # targetting only 7 digit pandigitals

    for i in list(p)[::-1]: #going in reversed to get the largest digit!
        number = int(''.join(i))
        if isPrime(number):
            return number

if __name__ == "__main__":
    print('Largest n-digit pandigital prime: {}'.format(compute()))
    


