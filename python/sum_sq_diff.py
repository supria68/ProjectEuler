"""
EP - 6
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2=385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2=55^2=3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

range_ip = int(input("Enter the end-limit: "))
sq_sum, total = 0,0

for i in range(1,range_ip + 1):
    sq_sum += i**2
    total += i
diff = total**2 - sq_sum


print("The sum of squares of first {} natural numbers: {}".format(range_ip,sq_sum))
print("The square of sum of first {} natural numbers: {}".format(range_ip,total**2))
print("The required difference: {}".format(diff))
