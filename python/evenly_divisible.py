"""
EP - 5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""

# lets calculate lcm of 1..20
def lcmFn(a,b):
    if a > b:
        greater = a
    else:
        greater = b

    while True:
        if greater % a == 0 and greater % b == 0:
            lcm = greater
            break
        else:
            greater += 1
    return lcm

if __name__ == "__main__":
    result = 1
    for i in range(2,21):
        result = lcmFn(result,i)
    print("Smallest positive number evenly divisible by all of 1..20: {}".format(result))
