"""
EP - 38

Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


Solution:
    1. the number must begin with a 9, x is not 9
    2. if 90 <= x < 100, then n1+n2+n3 = 90180360 an 8 digit number, so we can exclude this range as well
    3. if 900 <= x < 1000, then 90018003600; too many so they can be eliminated.
    4. if 9000 <= x < 10000, we have n1 + n2 = 900018000; a 9 digit
    So our range should be between 9000 and 10000
"""

def compute():
    largest_num = 918273645 # if 9 was choosen as x!
    for x in range(9000,10000):
        val = str(x) + str(x*2)
        if '0' not in val and len(set(val)) == 9: # checks if val is pandigital
            if int(val) > largest_num: # get only the largest val!
                largest_num = int(val)
    return largest_num

print(compute())
