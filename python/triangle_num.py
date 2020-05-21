"""
EP - 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?

"""

# A number x is said to be a triangular number iff 8x + 1 is perfect square for
# x < 2^53 - 1

import math

def charCount(ch):
    # This function returns the letter to number
    return (ord(ch) - 64)

def compute():
    f = open('p042_words.txt')
    words = f.read()
    f.close()

    word_list = words.strip().split(',') # list of words

    count = 0
    for word in word_list:
        #for each letter in word, find corresponding number and sum it (word count)
        num = sum(map(charCount, word[1:-1])) 
        if math.sqrt(8*num + 1) == int(math.sqrt(8* num + 1)): #check for perfect sqaure
            count += 1

    return count

if __name__ == "__main__":
    print(compute())
