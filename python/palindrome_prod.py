"""
EP - 4
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

palindrome_list = []
for i in range(100,1000):
    for j in range(100, 1000):
        prod = i * j
        palin = str(prod)[::-1]
        if str(prod) == palin:
            palindrome_list.append(prod)
print("Largest palindrome made from the product of 3 digit number: {}".format(max(palindrome_list)))
print("Number of two 3-digit products palindromes: {}".format(len(palindrome_list)))

