"""
EP - 22
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

# Function to determine the letter histogram
def score(names):
    count = 0
    names = names.replace("\"", "")
    for char in list(names): 
        count += alpha_dict[char]
    return count

if __name__ == "__main__":
    # Open file to read its content and store as list
    with open("names.txt",'r') as f:
        word_list = f.read().split(',')
        word_list.sort()

    #KNOWTHAT: python enumerate function adds indexing!!
    total = 0
    # alpha dictionary ~ histogram
    alpha_dict = {}
    for i,letter in enumerate(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),1):
        alpha_dict[letter] = i

    # call for name score function on entire list
    for i, names in enumerate(word_list,1):  # start at pos 1
        total += i * score(names)

    print("Total name score is {}".format(total))

