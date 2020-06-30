"""

EP - 28

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

def compute():
    """
    Solution:

    consider n * n outer spiral. (n = odd) 
    top right corner = n * n
    top left corner = (n * n) - (n-1)
    bottom left corner = (n * n) - 2(n-1)
    bottom right corner = (n * n) - 3(n-1)

    sum of this corners = 4 (n * n) - 6(n-1)

    repeat the same procedure for all inner spirals until the spiral size = 3!
    """
    
    num = 1001 # must always be odd
    result = 1 # to account for the 1 in the centre
    for i in range(3, num + 1, 2): # every odd step
        result += 4 * (i * i) - 6 * (i - 1)
    return result

if __name__ == "__main__":
    print("sum of the numbers on the diagonals in a 1001 by 1001 spiral is {}".format(compute()))
