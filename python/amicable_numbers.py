"""
EP - 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import math

def sumOfMultiples(num):
    total = 1
    limit = int(math.sqrt(num))
    # handling perfect square
    if num == limit * limit:
        total += limit
        limit -= 1
    
    for i in range(2,limit):
        if num % i == 0:
            total += i + num / i
    return total

    
def compute(limit):
    amicable_count = 0
    """
    This function checks if the two numbers are amicable and adds them.
    """
    for num in range(2, limit):
        a = sumOfMultiples(num)
        if a > num and a <= limit:
            if sumOfMultiples(a) == num:
                amicable_count += num + a
        
    return amicable_count

if __name__ == "__main__":
    result = compute(10000)
    print('Sum of amicable pairs less than 10000: {} '.format(result))
