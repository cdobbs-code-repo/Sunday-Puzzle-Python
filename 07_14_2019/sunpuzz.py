import enchant
import time
import capitals



start = time.time()

#---helper functions--BEGIN--#
def get_string(mylist):
        output = ""
        for x in mylist:
                output += x
        return output
#---helper functions----END--#

#open dictionary
d = enchant.Dict("en_US")

#get capitals
mycaps = capitals.get_capitals()

#zodiac signs
signs = ['leo','aries','taurus','gemini','virgo','libra','cancer']

word = ""
for places in mycaps:
	for z in signs:
		word = places + z
		#print current
		
		 
		
		#only continue IF word_len == 9
		if len(word) == 9:
			#print word
			# try all d placements

			#word = "romearies"

			#print d.check("dromedaries")

			word = list(word)

			for i in range(0,10):
				temp = word[:]
				temp.insert(i,'d')
				for j in range(0,11):
					temp2 = temp[:]
					temp2.insert(j,'d')
					#print str(temp2)
					if d.check(get_string(temp2)):
						print get_string(temp2)

## GET PROGRAM TIME
print "program execution time (sec):\n"
print time.time() - start
