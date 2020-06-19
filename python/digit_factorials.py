"""
EP - 34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def factorial(a):
    """
    This function computes the factorial of a number
    """
    if a == 0:
        return 1
    b = a
    for i in range(1,a):
        b = b * i
    return b

def compute():
    """
    This function checks whether
    numbers which are equal to the sum of the factorial of their digits.

    """
    total = 0 # holds the result
    for i in range(10,100000):
        sum_factorial = 0
        num = i # hold a copy
        while num > 0:
            d = int(num % 10)
            num = num // 10
            sum_factorial += factorial(d)
        if sum_factorial == i:
            total += i
    return total

if __name__ == "__main__":
    fn_result = compute()
    print('Total sum of digit factorials is : {}'.format(fn_result))
