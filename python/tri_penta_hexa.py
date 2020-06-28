"""
EP - 45

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.

#Solution:
    1. Hexagonal number is a subset of triangle number!
    2. Just substitue n = 2m - 1 in triangle equation.
    3. Check if this number is pentagon?

"""

import time, math

#Solution 
def compute():
    start = time.time() # begin execution
    
    def isPentagon(n):
        # A number x is pentagon if (sqrt(24x + 1) + 1) // 6 exists
        value = (math.sqrt(24 * n + 1) + 1) % 6
        if value == 0:
            return True
        else:
            return False
    
    num,result = 143, 0 # we want the next number which is triangle, hexagonal and pentagonal
    while True:
        num += 1
        result = num * (2* num - 1) # substitue n = 2m-1 in triangle equation
        if isPentagon(result):
            break
    end = time.time()

    print('Next triangle number that is also pentagonal and hexagonal : {}'.format(result))
    print('Exec time: {:f} seconds'.format(end- start))

if __name__ == "__main__":
    compute()
