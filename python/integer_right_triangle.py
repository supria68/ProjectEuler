"""
EP - 39 

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three max_periutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of max_periutions maximised?

############################################################################################
Solution: 
1. Check if a,b,c form a right triangle
2. Obtain the sets which provides the maximum perimeter.

Using pythagores Theorem, a^2 + b^2 = c^2, a+b+c = p, we can solve the above problem

c = p-b-a

substituting in the theorem, b= (p*(p-2a))/(2*(p-a))
since c < a + b, using symmetry, a = p/(2+sqrt(2))

Using these conditions for the values, we get a right triangle. Then the
solution is simple (just obtain the maximum value)

p will always be even no matter what the values are for a and b!
"""
import math

def compute():
    limit = 1000 
    sets, max_peri = 0,0 # sets = number of triangle sets, max_peri = maximum perimeter

    for p in range(limit//2, limit + 1, 2):
        temp = 0
        # Below 2 condition ensures we are looking at right triangle
        for a in range(2, int(p / (2+math.sqrt(2)))):
            if p*(p-2*a) % (2 * (p-a)) == 0:
                temp += 1
                if temp > sets:
                    sets, max_peri = temp, p
    return sets,max_peri

triangle_set, max_perimeter = compute()
print("Maximum perimeter is: {}".format(max_perimeter))
print("Triangle sets are : {} ".format(triangle_set))
