"""
EP - 66

Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.

"""

# Refer: 
#https://artofproblemsolving.com/wiki/index.php/Pell_equation
#http://www.ams.org/notices/200202/fea-lenstra.pdf

import math
largest_x, result = 0, 0

for D in range(2, 1001):
    S = int(math.sqrt(D))

    if S * S == D: continue

    # Initial values for convergence
    m, d, a = 0, 1, S
    n1, n0, d1, d0 = 1, a, 0, 1


    while n0*n0 - D*d0*d0 != 1:
        m = int(d * a - m)
        d = (D - m*m) // d
        a = (S + m) // d
        #print(m,d,a)
        n2, n1 = n1, n0
        d2, d1 = d1, d0

        n0 = a * n1 + n2
        d0 = a * d1 + d2
        #print(n0,d0)
        
    if n0 > largest_x:
        largest_x = n0
        result = D

print("Result: {}".format(result))

