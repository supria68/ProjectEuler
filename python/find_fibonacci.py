"""
EP - 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?
"""

def fibonacci(limit):
    # This function generates the fibonacci series until
    # an element in this series contain 1000 digits.
    fib_list = [1,1]
    F1, F2 = 1, 1
    while True:
        total = F1 + F2
        fib_list.append(total)
        if len(str(total)) == limit:
            val = fib_list.index(total)+1 # python has 0 indexing!!
            break
        F2, F1 = total, F2
    return val,fib_list # return the sequence and the index

if __name__ == "__main__":
    limit = 1000
    index, fib_seq = fibonacci(limit)
    print("The first term in the Fibonacci sequence to contain 1000 digits is at {} location".format(index))
    print("First 20 Fibonacci Sequence {}".format(fib_seq[:20]))
