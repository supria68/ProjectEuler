"""
EP - 52

It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

if __name__ == "__main__":
    x = 1
    #print('Begin execution')
    while True:
        if set(str(x)) == set(str(x*6)):
            if set(str(x)) == set(str(x*5)):
                if set(str(x)) == set(str(x*4)):
                    if set(str(x)) == set(str(x*3)):
                        if set(str(x)) == set(str(x*2)):
                            print ('Smallest positive integer: {}'.format(x))
                            break
        x += 1
    #print('end')

