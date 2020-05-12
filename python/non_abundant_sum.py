"""
EP - 23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
import math

def divisorSum(num):
    #This function computes the sum of divisors
   
    if num == 1:
        return 1  # 1 doesnt have any divisors
    total = 1 
    div = 2 #lets start from 2
    while div < math.ceil(math.sqrt(num)):
        if num % div == 0:
            total += div  #sum of all divisors
            total += num // div # is needed as limit is sqrt(num)
        div += 1
    if math.ceil(math.sqrt(num)) ** 2 == num: # handles the perfect square cases
        total += math.ceil(math.sqrt(num))
    return total

if __name__ == "__main__":

    abundant_num = []
    # Check for all numbers <= 28123 if they are abundant numbers
    for i in range(1, 28123): 
        if divisorSum(i) > i:
            abundant_num.append(i)
    
    # sum_list holds the posible sum of two abundant numbers
    sum_list = [0]*28124
    for x in range(len(abundant_num)):
        for y in range(x, len(abundant_num)):
            abundant_sum = abundant_num[x] + abundant_num[y] 
            if abundant_sum <= 28123:
                sum_list[abundant_sum] = abundant_sum
    
    # Iterate over sum_list to find the sum of all postive non abundant integers 
    ans = 0
    for j in range(1,len(sum_list)):
        if sum_list[j] == 0:    
            ans += j
    print("sum of all the positive integers which cannot be written as the sum of two abundant numbers: {}".format(ans))

