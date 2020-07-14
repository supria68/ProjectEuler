"""
EP - 99

Comparing two numbers written in index form like 2^11 and 3^7 is not difficult, as any calculator would confirm that 2^11 = 2048 < 3^7 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

"""

import math

def compute():
    """
    Solution is pretty simple.

    a^b > x^y
    => b* log(a) > y* log(x)

    1. compute the logarithmic values of base - exponents pairs
    2. iterate over the log values to get the location with greatest value.

    """
    data = {}

    # Reading the file
    with open('p099_base_exp.txt') as f:
        for idx, line in enumerate(f):
            base, exp = line.split(',')
            data[idx] = int(exp) * math.log(int(base))

    max_value = data[0] # assume thats the greatest value
    max_loc = 0

    for k, v in data.items():
        if v > max_value:
            max_loc = k
            max_value = v

    return (max_loc + 1) # indexing at 0 in python
     
print(compute())
