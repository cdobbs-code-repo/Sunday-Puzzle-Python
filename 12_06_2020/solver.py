import enchant

# instantiate dictionary
mydict = enchant.Dict("en-US")

# GLOBALS # GLOBALS # GLOBALS #
sym_letters = "loiumntvwx"
opp_letters = ["pq","qp","db","bd"]


def is_reflective_word(word: str) -> bool:
    count1 = 0
    count2 = -1
    while (count1+1)*2 <= len(word):
        temp = word[count1] + word[count2]
        if word[count1] not in sym_letters:
            if temp not in opp_letters:
                return False
        else:
            if word[count1] != word[count2]:
                return False
        count1 += 1 
        count2 -= 1
    return True


# TASK:
# -Find 6 letter words with an indentical reflection

# Attempt number 1: just try sym_letters for all 6

# for a in sym_letters:
#     for b in sym_letters:
#         for c in sym_letters:
#             for d in sym_letters:
#                 for e in sym_letters:
#                     for f in sym_letters:
#                         temp = a+b+c+d+e+f
#                         if is_reflective_word(temp):
#                             if mydict.check(temp):
#                                 print(temp)
# print("attempt ONE complete\n")

# Attempt number 2: add one pair of opp letters

# for a in sym_letters:
#     for b in sym_letters:
#         for c in sym_letters:
#             for d in sym_letters:
#                 for x in opp_letters:
#                     temp1 = x[0]+a+b+c+d+x[1]
#                     temp2 = a+x[0]+b+c+x[1]+d
#                     temp3 = a+b+x[0]+x[1]+c+d
#                     if is_reflective_word(temp1):
#                         if mydict.check(temp1):
#                             print(temp1)
#                     if is_reflective_word(temp2):
#                         if mydict.check(temp2):
#                             print(temp2)
#                     if is_reflective_word(temp3):
#                         if mydict.check(temp3):
#                             print(temp3)
# print("attempt TWO complete\n")

# Attempt number 3: just try all letters

alph = "abcdefghijklmnopqrstuvwxyz"
for a in alph:
    for b in alph:
        for c in alph:
            for d in alph:
                for e in alph:
                    for f in alph:
                        temp = a+b+c+d+e+f
                        if is_reflective_word(temp):
                            if mydict.check(temp):
                                print(temp)
print("attempt THREE complete\n")
