"""
EP - 48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def compute():
    total = 0
    for i in range(1, 1001):
        total += i**i
    return (total % 10**10) #getting only last 10 digits

print(compute())
