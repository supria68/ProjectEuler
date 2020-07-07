"""
EP - 60

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""
import math

def sieve(limit):
    """
    Use Sieve of Erotosthenes to generate prime
    """
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

def isPrime(n):
    """
    Function to check if the number is prime
    """
    if n <= 1 : return False
    if n == 2 or n == 3: return True
    if n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, math.ceil(math.sqrt(n)), 2):
        if n % i == 0:
            return False
    return True

def perm(a,b):
    """
    Generate all posible permutations of number (a,b) and check if they are
    primes.

    Eg: a = 2, b = 3, perm(a,b) = [23,32]
    Check if 23 and 32 are prime??
    """
    val1 = int(str(a) + str(b))
    val2 = int(str(b) + str(a))
    
    if isPrime(val1) and isPrime(val2):
        return True
    return False

def compute():
    primes = sieve(10000) # limit
    """
    1. let a = first element of list "primes"
        b = is the second element of list "primes" (b > a)
        check if permutations of (a,b) are prime
    2. If prime, c = third element of list "primes" (c > b)
        check if permutations of (a,c), (b,c) are prime
    3. If prime, d = fourth element of list "primes" (d > c)
        check if permutations of (a,d), (b,d), (c,d) are prime
    4. If prime, e = fifth element of list "primes" (e > d)
        check if permutations of (a,e), (b,e), (c,e), (d,e) are prime

        If prime, add everything! (our result)
    """
    for a in primes:
        for b in primes:
            if b < a: continue
            if perm(a,b):
                for c in primes:
                    if c < b: continue
                    if perm(a,c) and perm(b,c):
                        for d in primes:
                            if d < c: continue
                            if perm(a, d) and perm(b, d) and perm(c, d):
                                for e in primes:
                                    if e < d: continue
                                    if perm(a, e) and perm(b, e) and perm(c, e) and perm(d, e):
                                        return a+b+c+d+e


if __name__ == "__main__":
    print(compute())
                        
