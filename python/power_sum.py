"""
EP - 16
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def powerSum(num):
    num = list(str(num))
    total = 0
    for i in num:
        total += int(i)
    return total

"""
Option:2
def powerSum(num):
    num = list(map(int,list(str(num))))
    return sum(num)
"""
print("The power digit sum is {}".format(powerSum(2**1000)))

