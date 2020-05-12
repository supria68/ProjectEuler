"""
EP - 12

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
"""
import math, itertools

def divisors(num):
    # This function checks for number of divisors
    count = 0
    limit = math.ceil(math.sqrt(num))
    count = sum(2 for i in range(1, limit) if num % i ==0)
    if limit**2 == num:
        # remove extra divisor (5*5 = 25)
        count -= 1
    return count

def triangleNum():
    triangle_num = 0
    for i in itertools.count(1): # By using itertools, memory is saved, fasterexecution
        triangle_num += i
        if divisors(triangle_num) > 500: # check for > 500 divisors
            return triangle_num

if __name__ == "__main__":
    print(triangleNum())
    


