"""

EP - 57

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

By expanding this for the first four iterations, we get:

3/2, 7/5, 17/12, 41/29.

The next three expansions are 99/70, 239/169, and 577/408, but the eighth
expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?

"""

# Check this link for detailed explanation on continued fractions:
# https://math.stackexchange.com/questions/730349/convergents-of-square-root-of-2

def compute():
    p, q = 1, 1

    result = 0

    for i in range(1000):
        num = p + 2 * q
        den = p + q

        if len(str(num)) > len(str(den)):
            result += 1
        p = num
        q = den

    return result

print(compute())
