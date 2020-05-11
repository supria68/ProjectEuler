"""
EP- 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below 2000000.

Solution:
    Since the upper limit is extremely large, cost = O(n^3)...
    Use "Sieve of Eratosthenes" to solve this problem

Algorithm:
    1. Create a list l of consecutive integers {2,3,…,N}.
    2. Select p as the first prime number in the list, p=2.
    3. Remove all multiples of p from the l.
    4. set p equal to the next integer in l which has not been removed.
    5. Repeat steps 3 and 4 until p2 > N, all the remaining numbers in the list are primes

"""

def prime(limit):
    # declare an empty set to hold all the multiple values
    multiple = set()

    # iterate over 2,3...limit
    # we need to save as much memory as possible as limit is extremely high!! 
    # Lets use generators and yeild rather than iterables and return
    # generators - iterate only once, dont store values in memory
    # yield - return generator object

    for i in range(2, limit + 1):
        if i not in multiple:
            yield i 
        
        # add all multiples of i to set
        multiple.update(range(i*i,limit+1,i))
    
if __name__ == "__main__":
    total = 0
    limit = 2000000
    prime_list = list(prime(limit))
    print("Sum of all primes below {} is {}".format(limit,sum(prime_list)))
