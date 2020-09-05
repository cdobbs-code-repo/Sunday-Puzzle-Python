

import re
import time

# start the timer to get program execution speed
start = time.time()

# 05_06_2018 weekly sunday puzzle

# MAIN STEPS
# 1. iterate through all words in the dictionary (length > 6?)
# 2. for each word, check if word[2:-1] is a country

# first, get all countries
def get_countries():
    output = []
    with open ("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/05_06_2018/countries.csv", "r") as BigFile:
        data=BigFile.readlines()
    for i in range(len(data)):
        mylist = re.split('"', data[i])
        output.append(mylist[1].lower())
    return output	
foo = get_countries()
#ignore ones with spaces for now
bar = []
for x in foo:
    if " " not in x:
        bar.append(x.lower())

# open our dictionary
filer = open("C:/Users/cdobb/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")

# iterate through dictionary
for word in filer:
    if "/" in word:
        word = word.split("/")[0]
    word = word.lower()
    # find dictionary word(s) where 3rd to 2nd to last letters spell a country
    for x in bar:
        if word[2:-1] == x:
            print(word)


## GET PROGRAM TIME
print("program execution time (sec):")
print(time.time() - start)
