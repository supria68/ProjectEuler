"""
EP-3
What is the largest prime factor of the number 600851475143 ?
"""
import math
prime_list = []
num = 600851475143 

def prime_factors(num):
    num_rt = math.floor(math.sqrt(num))
    i = 2
    while i <= num_rt:
        if num % i == 0: # checks if i is prime
            while num % i == 0: # This loop removes the composites!
                num = num / i
            prime_list.append(i) # list holds only prime numbers
        i += 1
  
    return max(prime_list) 
print(prime_factors(num))

        

