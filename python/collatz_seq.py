"""
EP - 14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

"""
def collatz(num):
    # This function returns the collatz sequence for a given number
    mylist = []
    while num > 1:
        #print(num)
        mylist.append(num)
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3 * num + 1
    return mylist

if __name__ == "__main__":
    count = 0
    for i in range(1000000):
        num = collatz(i)
        if len(num) > count:
            count = len(num) + 1 # to include 1
            val = num[0] # number which produced the longest sequence
    print(val)


        

