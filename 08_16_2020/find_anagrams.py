
import re

french_list = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/08_16_2019/cities_in_france_pop_100000plus.txt")

for foo in french_list:
    italian_list = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/08_16_2019/cities_in_italy_pop_100000plus.txt")
    for bar in italian_list:
        foo = foo.strip()
        bar = bar.strip()
        foo = foo.replace(" ","")
        bar = bar.replace(" ","")
        foo = foo.lower()
        bar = bar.lower()
        if len(foo) == len(bar):
            anagram_bool = 0
            for lett in foo:
                if lett in bar:
                    anagram_bool += 1
            if anagram_bool == len(foo):
                print(foo + ", " + bar)
    italian_list.close()
french_list.close()
