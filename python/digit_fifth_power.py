"""
EP - 30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def fifth_power(num):
    # function to compute the fifth power and sum it
    return sum(int(i)**5 for i in list(str(num)))

if __name__ == "__main__":
    total = 0
    for x in range(2,1000000):
        if x == fifth_power(x):
            total += x
    print(" sum of all the numbers that can be written as the sum of fifth powers of their digits: {}". format(total))

