"""
EP - 63

The 5-digit number, 16807=7^5, is also a fifth power. Similarly, the 9-digit
number, 134217728=8^9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

# Solution:
    we need an integer x such that: 10^(n-1) <= x < 10^n
    Our lower bound -> 10^(n-1)/n
    Upper bound -> 10 (cause 10^2 = 100(2 digit --> 3 digit))

"""
import math
def compute():
    limit, n = 0,1 # start from 1
    result = 0
    while limit < 10:
        limit = math.ceil(math.pow(10,(n-1.0)/n)) #upper bound
        result += 10 - limit #takes care when lower bound > upper bound!
        n += 1
    return result

if __name__ == "__main__":
    print(compute())
