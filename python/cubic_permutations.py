"""
EP - 62

The cube, 41063625 (345^3), can be permuted to produce two other cubes:
56623104 (384^3) and 66430125 (405^3). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""

def compute():
    cubes = [] # holds the bunch of cubes
    i = 0 # begin with 0
    
    """
    1. start with the cube of the number (i)
    2. store the cube of (i) as a list in ascending order (num)
    3. Append to the list (cubes)
    4. When count of (num) reaches 5 in (cubes) list! --> thats our result!
    """
    while True:
        num = sorted(list(str(i**3))) 
        cubes.append(num) 
        if cubes.count(num) == 5: 
            return ((cubes.index(num))**3)
            break
        i += 1

print(compute())
