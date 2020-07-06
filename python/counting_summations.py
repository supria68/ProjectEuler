"""
EP -76

It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?

"""

def compute(limit):
    # Solution is similar to EP - 31.

    ways = [1] + [0]*limit

    for i in range(1,limit):
        for j in range(i, limit + 1):
            ways[j] += ways[j-i]

    return ways[limit]

#print(compute(5))
print(compute(100))
