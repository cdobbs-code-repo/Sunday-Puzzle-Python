import time
import enchant

def vowels_in_word(word: str) -> bool:
    vowels = "aeiouy"
    for vowel in vowels:
        if vowel in word:
            return True
    return False

# def no_odd_repeats(word: str) -> bool:
#     odd_repeats = ["aa","ii","qq",""]

start_time = time.time()

diction = enchant.Dict("en-US")

foo = "horn"
alph = "abcdefghijklmnopqrstuvwxyz"

for x in alph:
    for y in alph:
        temp = x+y
        for i in range(0,len(foo)+1):
            bar = foo[:i]+temp+foo[i:]
            for k in range(0,len(bar)+1):
                bar2 = bar[:k]+temp+bar[k:]
                for m in range(0,len(bar2)+1):
                    bar3 = bar2[:m]+temp+bar2[m:]
                    for j in range(1,len(bar3)-1):
                        thing1 = bar3[:j]
                        thing2 = bar3[j:]
                        if vowels_in_word(thing1) and vowels_in_word(thing2):
                            if diction.check(thing1) and diction.check(thing2):
                                print(thing1 + " " + thing2 + " with " + temp)

print("\n-------------------\n--TIME (sec) = " + str(time.time()-start_time)[:6])