"""
EP - 36

The decimal number, 585 = (1001001001)2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def palindrome(num):
    # function to check if number is palindrome
    rev_num = str(num)[::-1]
    if rev_num == str(num):
        return True
    else:
        return False

def compute():
    total = 0
    for num in range(1, 1000000):
        if (palindrome(num) and palindrome(bin(num).split('b')[1])):  
            total += num
    return total

if __name__ == "__main__":
    print(compute())
    
