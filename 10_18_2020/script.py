import enchant

#helper function - checks if word is composed only of lowercase letters
def only_letters(word):
    alphi = "abcdefghijklmnopqrstuvwxyz"
    for x in word:
        if x not in alphi:
            return False
    return True

# dictionary variable below used for .check function to see if words exist
mydict = enchant.Dict("en-US")

# opening provided text document that contains a list of all world capitals
foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/10_18_2020/list_of_capitals.txt")

# for every world capital in our list...
for bar in foo:
    # making next capital lower case and cutting of newline char
    bar = bar.lower()[:-1]
    # if no spaces, punctuation, or special characters...
    if only_letters(bar):
        # try removing a letter and inserting "dy" into every locating from 2 letter to second last
        for i in range(1,len(bar)-1):
            temp1 = bar[:i] + "d"
            temp2 = "y" + bar[i+1:]
            temp3 = temp1 + temp2
            # try splitting new string ever place from 3rd letter to second last
            # to check and see if resulting strings are real words
            for x in range(2,len(temp3)-1):
                temp1 = temp3[:x]
                temp2 = temp3[x:]
                # if resulting two strings are in the dictionary, then print them out
                if mydict.check(temp1):
                    if mydict.check(temp2):
                        print(bar)
                        print(temp1)
                        print(temp2)
                        print("-----------------------")
