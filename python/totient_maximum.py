"""
EP - 66

Euler’s Totient function, φ(n) [sometimes called the phi function], is used to determine the number of numbers less than n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

n	Relatively Prime	φ(n)	n/φ(n)
2	1   	                1	2
3	1,2	                2	1.5
4	1,3	                2	2
5	1,2,3,4	                4	1.25
6	1,5	                2	3
7	1,2,3,4,5,6	        6	1.1666…
8	1,3,5,7	                4	2
9	1,2,4,5,7,8	        6	1.5
10	1,3,7,9	                4	2.5
It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

# Solution: Use the euler's product formula to solve this problem
# https://en.wikipedia.org/wiki/Euler's_totient_function

#For n/φ(n) to be maximum, the number must have distinct small prime factors =>
#multiply primes until largest number less then 1.000.000 is reached.

def Sieve(limit):
    multiple = set()
    primes = []

    for i in range(2, limit + 1):
        if i not in multiple:
            primes.append(i)

        # add all multiples of i to set
        multiple.update(range(i*i,limit+1,i))
    return primes

def compute():
    result, idx = 1, 0
    limit = 1000000
    prime = Sieve(200)

    while result * prime[idx] < limit :
        result *= prime[idx]
        idx += 1

    return result

print(compute())
    
