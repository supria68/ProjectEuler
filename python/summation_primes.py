"""
EP- 10

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below 10000.

"""
def prime(start,limit):
    total = 0
    for num in range(start, limit + 1):
        count = 0
        # lets check if the number has any divisors other than itself
        for i in range(2, (num//2 + 1)):
            if num % i == 0:
                count += 1
                break
            # No divisors other than itself? then its prime!
            if count == 0 and num != 1:
                total += num
    return total

"""
option 2:
    
numbers = list(range(2,limit))

for prime in numbers:
    for x in numbers:
        if x % prime == 0 and x != prime:
            numbers.remove(x)
            
print("Sum of all primes below {} is {}".format(limit,sum(numbers)))
"""
                
if __name__== "__main__":
    limit = 10000 # 2 million
    print("Sum of all primes below {} is {}".format(limit,prime(2,limit)))
