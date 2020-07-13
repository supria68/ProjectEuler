"""

EP - 100

If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 1012 = 1,000,000,000,000 discs in total, determine the number of blue discs that the box would contain.


#### Solution:

1. b + r > 10^ 12, b > 0 and r > 0. Both b and r are integers!
2. From first arrangement, [b / (b + r)] * [(b-1) / (b+r-1)] = 1/2
    Solving this using quadratic equation:

    b = r + (1/2)*(1 + sqrt(8*r^2 + 1))
    But what should be the value of r??
    
3. Also using quadratic diophantine equation (wolfram alpha), 
    b (next) = 3 b(previous) + 2 r(previous) - 2
    r (next) = 4 b(previous) + 3 r(previous) - 3

"""
import math

def compute():

    b, r = 15, 21 

    while r < math.pow(10,12):
        b_temp = 3 * b + 2 * r - 2
        r_temp = 4 * b + 3 * r - 3
        
        b = b_temp
        r = r_temp
    return b

print(compute())
