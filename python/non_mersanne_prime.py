"""
EP - 97

The first known prime found to exceed one million digits was discovered in
1999, and is a Mersenne prime of the form 2^6972593−1; it contains exactly
2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains
2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.

## Solution:
    Since 2^7820457 takes a long time to compute, we can make use of
    pow(a,b,[z]) to figure out the result!

    Use mod by 10**10 to scale the values.
"""

def compute(a,b,c,m):
    result = (c * pow(a,b,m) + 1) % m
    return result

if __name__ == "__main__":
    ans = compute(2, 7830457, 28433, 10**10)
    print("last 10 digits: %010d", ans) #last 10 digits
