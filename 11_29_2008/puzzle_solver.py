
import enchant

mydict = enchant.Dict("en-US")

# import criminal words
criminal_words_file = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2008/criminal_words.txt")
criminal_words = criminal_words_file.read()
criminal_words = criminal_words.split("\n")
criminal_words_file.close()

def criteria_met(word):
    # drop first letter
    word = word[1:]
    for i in range(0,len(word)):
        temp = word[:i] + word[i+1:]
        if temp in criminal_words:
            print(temp)
            return True
        if mydict.check(temp):
            print(temp)
    return False


for bar in criminal_words:
    try:
        if bar[0] == "s":
            if criteria_met(bar):
                print(bar)
    except:
        pass

# mugger
# smuggler