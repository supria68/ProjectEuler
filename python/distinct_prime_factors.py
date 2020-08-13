"""
EP - 47

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?
"""

def factorCount(num):
    # returns the number of prime factors
    i = 2
    prime = set()
    while i < num ** 0.5 or num == 1:
        if num % i == 0:
            num = num / i
            prime.add(i)
            i -= 1
        i += 1
    return (len(prime) + 1) # we will only have 1 prime after sqrt of number!

def compute():
    # brute force algorithm to get the result

    p = 2 * 3 * 5 * 7 #product of first four primes

    while True:
        if factorCount(p) == 4:
            p += 1
            if factorCount(p) == 4:
                p += 1
                if factorCount(p) == 4:
                    p += 1
                    if factorCount(p) == 4:
                        return p-3
        p += 1

if __name__ == "__main__":
    print(compute())

