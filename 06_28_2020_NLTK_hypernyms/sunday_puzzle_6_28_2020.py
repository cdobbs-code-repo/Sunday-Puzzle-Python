import enchant
from nltk.corpus import wordnet
import time
import fileinput

#import txt of all words already checked so we don't recheck them
file = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/words_already_used.txt")
checked_wordbank = file.readlines()
checked_wordbank = str(checked_wordbank)
file.close()

start_time =time.time()

alph = "abcdefghijklmnopqrstuvwxyz"

def word_already_checked(myword):
    return (myword in checked_wordbank)

def is_animal(myword):
    foo = wordnet.synsets(myword)
    hyp = lambda s:s.hypernyms()
    try:
        bar = str(list(foo[0].closure(hyp)))
    except:
        print("the troublesome word is " + myword)
    return ("animal" in bar)

def next_let(foo):
    if foo != 'z':
        return alph[alph.index(foo)+1]
    return 'X'  #returning X just to simply fail word check

dictio = enchant.Dict("en_US")

for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    temp = a+b+c+d+e
                    if not word_already_checked(temp) and wordnet.synsets(temp) != [] and is_animal(temp): # and dictio.check(a+b) and dictio.check(d+e):
                        print(temp + ", " + a + b + ", " + d + e)

## GET PROGRAM TIME
print("program execution time (sec):\n")
print(time.time() - start_time)
