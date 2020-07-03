"""

EP - 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?

"""
def sieve(limit):
   # Using Sieve of Erathoneses to generate all primes
    prime = [2]
    is_prime = [True] * limit
    is_prime[0] = False
    is_prime[1] = False
    is_prime[2] = True
    for i in range(3, int(limit**0.5 + 1), 2):
        idx = i*2
        while idx < limit:
            is_prime[idx] = False
            idx += i
    for i in range(3, limit, 2):
        if is_prime[i]:
            prime.append(i)
        
    return prime


def compute():
    # prime numbers upto 1 million
    primes = sieve(1000000)

    length, consecutive = 0, 0 # length of consecutive sum, consecutive prime sum

    sec_limit = len(primes)

    for i in range(len(primes)):
        for j in range(i + length, sec_limit):
            sol = sum(primes[i:j])
            if sol < 1000000:
                if sol in primes:
                    length = j-i
                    consecutive = sol
            else:
                sec_limit = j+1
                break
    return consecutive

print(compute())
