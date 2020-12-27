
def is_palindrome(word):
    # racecar 
    iter1 = 0
    iter2 = len(word) - 1
    while iter1 < iter2:
        if word[iter1] != word[iter2]:
            return False
        iter1 += 1
        iter2 -= 1
    return True

# we need a palindrome that's 7 letters
# and that alternates as a two word phrase with minor changes

# # get all 7 letter palindromes first...
# out5 = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/12_27_2020/five_letter_words.txt","w")
# out2 = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/12_27_2020/two_letter_words.txt","w")
# file = open("C:/Users/cdobb/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")
# #---------------------------------

# for line in file:
#     # remove all extra characters and flag non alphabetical characters
#     if "/" in line:
#         line = line[0:(line.index("/"))]
#     line = line.lower()
#     if "\n" in line:
#         line = line[0:(line.index("\n"))]

#     if len(line) == 5:
#         out5.write(line + "\n")
    
#     if len(line) == 2:
#         out2.write(line + "\n")

alph = "abcdefghijklmnopqrstuvwxyza"
# NOW find that palindrome!
fivers = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/12_27_2020/five_letter_words.txt")
for fiver in fivers:
    fiver = fiver.strip()
    twoers = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/12_27_2020/two_letter_words.txt")
    for twoer in twoers:
        twoer = twoer.strip()
        try:
            if alph[alph.index(twoer[-1])+1] == fiver[0]:
                if is_palindrome(fiver+twoer[0]+fiver[0]):
                    print(fiver)
                    print(twoer)
        except:
            foo = 42 # break here
    twoers.close()
fivers.close()





