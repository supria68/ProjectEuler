"""
EP - 17

If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

def numDict():
    # let's generate a number-letter dictionary from 1 to 1000
    dic = {}
    for i in range(0, 1001):
        dic[i] = 0 

    # store the number-letter count from 0 - 19
    dic[0] = 0
    dic[1] = 3
    dic[2] = 3
    dic[3] = 5
    dic[4] = 4
    dic[5] = 4
    dic[6] = 3
    dic[7] = 5
    dic[8] = 5
    dic[9] = 4
    dic[10] = 3
    dic[11] = 6
    dic[12] = 6
    dic[13] = 8
    dic[14] = 8
    dic[15] = 7
    dic[16] = 7
    dic[17] = 9
    dic[18] = 8
    dic[19] = 8

    # store the num-letter count for multiples of tens < 100
    dic[20] = 6
    dic[30] = 6
    dic[40] = 5
    dic[50] = 5
    dic[60] = 5
    dic[70] = 7
    dic[80] = 6
    dic[90] = 6

    return dic

def compute():
    num_dic = numDict()

    for i in range(21, 100):                        # Eg: i = 23
        tens = (i // 10) * 10                       # tens = 20
        units = i - tens                            # units = 3
        num_dic[i] = num_dic[tens] + num_dic[units] # num_dic[23] = 6 + 5
    
    for i in range(100, 1000):                      # Eg: i = 125
        ones = (i // 100)                           # ones = 1
        rest = i - ones * 100                    # rest = 25
        
        # we need to add an extra "and" term
        if rest == 0:
            num_dic[i] = num_dic[ones] + 7 # (all hundred) 100, 200, 300, ..900
        else:
            num_dic[i] = num_dic[ones] + 10 + num_dic[rest] # num_dic[125] = num_dic[1] + "hundred and" + num_dic[25]

    num_dic[1000] = 11 # one thousand
    
    return sum(num_dic.values()) #returns the sum of all values in dictionary

if __name__ == "__main__":
    print(compute())
    
