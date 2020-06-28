

import enchant

d = enchant.Dict("en_US")

#---helper functions----#

def opp_letter(vi):
	if vi == 'a':
		return 'z'
	if vi == 'b':
                return 'y'
        if vi == 'c':
                return 'x'
        if vi == 'd':
                return 'w'
        if vi == 'e':
                return 'v'
        if vi == 'f':
                return 'u'
        if vi == 'g':
                return 't'
        if vi == 'h':
                return 's'
        if vi == 'i':
                return 'r'
        if vi == 'j':
                return 'q'
        if vi == 'k':
                return 'p'
        if vi == 'l':
                return 'o'
        if vi == 'm':
                return 'n'
        if vi == 'n':
                return 'm'
        if vi == 'o':
                return 'l'
        if vi == 'p':
                return 'k'
        if vi == 'q':
                return 'j'
        if vi == 'r':
                return 'i'
        if vi == 's':
                return 'h'
        if vi == 't':
                return 'g'
        if vi == 'u':
                return 'f'
        if vi == 'v':
                return 'e'
        if vi == 'w':
                return 'd'
        if vi == 'x':
                return 'c'
        if vi == 'y':
                return 'b'
        if vi == 'z':
                return 'a'

#---helper functions----#

alpha = "abcdefghijklmnopqrstuvwxyz"

for let in alpha:
	for let2 in alpha:
		for let3 in alpha:
			word = let+let2+let3+opp_letter(let3)+opp_letter(let2)+opp_letter(let)
			if d.check(word):
				print(word)
