from PyDictionary import PyDictionary
import enchant
from nltk.corpus import wordnet
import time
import fileinput

start_time =time.time()

alph = "abcdefghijklmnopqrstuvwxyz"

def word_already_checked(myword):
    return (myword in checked_wordbank)

def is_animal(myword):
    foo = wordnet.synsets(myword)
    hyp = lambda s:s.hypernyms()
    bar = ""
    try:
        bar = str(list(foo[0].closure(hyp)))
    except:
        pass#print("the troublesome word is " + myword)
    return ("animal" in bar)

def next_let(foo):
    if foo != 'z':
        return alph[alph.index(foo)+1]
    return 'X'  #returning X just to simply fail word check

#--------globals------------------
dictionary = PyDictionary()
output = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_08_2008/animal_list.txt","w")
dictio = enchant.Dict("en_US")
alph = "abcdefghijklmnopqrstuvwxyza"
nums = "0123456789"
myfile = open("C:/Users/cdobb/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")
#---------------------------------

# sort through dicitonary
for line in myfile:
    # remove all extra characters and flag non alphabetical characters - START
    if "/" in line:
        line = line[0:(line.index("/"))]
    line = line.lower()
    if "/n" in line:
        line = line[0:(line.index("/n"))]
    letts = True
    for lett in line:
        if lett not in alph:
            letts = False
    numbers = False
    for each in nums:
        if each in line:
            numbers = True
    # remove all extra characters and flag non alphabetical characters - END

    # if no number, all letters, and word length above 3 continue
    if not numbers and letts and len(line) > 3:
        # now ensure the word is an animal
        if is_animal(line): # and dictio.check(a+b) and dictio.check(d+e):
            output.write(line+"\n")

## GET PROGRAM TIME
print("program execution time (sec):\n")
print(time.time() - start_time)
