import cmudict
from PyDictionary import PyDictionary

pydict = PyDictionary()

def three_i(bar):
    count = 0
    for x in bar:
        if x == "i":
            count += 1
    return (count == 3)

foo = open("C:/Users/cdobb/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")

# First we are simply finding words of length 8 with 3 i letters
# -- some preprocessing of the dictionary entries is involved --
for bar in foo:
    bar = bar.split("/")[0]
    if "\n" in bar:
        bar = bar[:-2]
    bar = bar.lower()
    if len(bar) == 8 and three_i(bar):
        # now we look at pronunciation with cmudict...
        temp = 0
        try:
            temp = cmudict.words().index(bar)
        except:
            temp = -1
        if temp >= 0:
            temp = cmudict.entries()[temp]
            temp = temp[1]
            #now check each syllable...
            no_i_sound = True
            for syl in temp:
                if "IH" in syl or "AY" in syl:
                    no_i_sound = False
                    break
            if no_i_sound:
                # finally we want to get rid of names or obscure words by just checking
                # to see if PyDictionary recognizes it...
                meaning = pydict.meaning(bar, disable_errors=True)
                if meaning != {} and type(meaning) != type(None):
                    print(bar)

foo.close()