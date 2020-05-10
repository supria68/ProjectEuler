"""
EP- 20
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""

def factSum(num):
    fact = 1
    for i in range(1,num+1):
        fact *= i
    return sum(list(map(int,list(str(fact)))))

print("sum of the digits in the number 100!: {}".format(factSum(100)))
