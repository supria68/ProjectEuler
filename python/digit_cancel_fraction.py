"""
EP - 33

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""
def gcd(a,b):
    # compute the highest common factor!
    while (b):
        a, b = b, a % b
    return a

def compute():
    """
    Let's use the brute-force method to find the solution
    The solution will be of the form (10n+i)/(10i+d) = n/d
    where n < d < i

    """
    n,d = 1,1
    for i in range(1,10):
        for den in range(1,i):
            for num in range(1,den):
                if den * (10 * num + i) == num * (10 * i + den):
                    d *= den
                    n *= num
    result = d / gcd(n,d) 
    return result

print('Product of denominators: {}'.format(compute()))
