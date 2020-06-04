"""
EP - 65

What is most surprising is that the important mathematical constant,
e=[2;1,2,1,1,4,1,1,6,1,...,1,2k,1,...].

The first ten terms in the sequence of convergents for e are:

2,3,8/3,11/4,19/7,87/32,106/39,193/71,1264/465,1457/536,...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
"""

def factor(k):
    if k == 0:
        return 2
    elif k % 3 == 2:
        return k // 3 * 2 + 2
    else:
        return 1

def compute():
    """
    numerator, denominator = factor(i) * numerator + denominator, numerator
    Also, factor(i) = 2, if i = 0
                    = i // 3 * 2 + 2 , if i % 3 == 2  
                    = 1, elsewhere
    """
    numerator, denominator = 1, 0
    total = 0

    for i in range(99,-1,-1): #reversed(range(100))
        numerator, denominator = factor(i) * numerator + denominator, numerator

    for c in str(numerator):
        total += int(c)
    return total

print(compute())
