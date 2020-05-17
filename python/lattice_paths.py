"""
EP - 15
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import math

# This problem is a case of combination scenario. 
def binomial(n, k):
	assert 0 <= k <= n #helps detect problem early. 
	return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

if __name__ == "__main__":
    print(binomial(40,20))

