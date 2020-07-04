import re


def get_capitals():
    output = []
    with open ("countries.csv", "r") as BigFile:
        data=BigFile.readlines()


    for i in range(len(data)):
        #print "Line No- ",i 
        #print data[i]
        mylist = re.split('"', data[i])
	matcher = re.search('\xc3',mylist[3])
	#matcher2 = re.search(".", mylist[3])
	#matcher3 = re.search("'",mylist[3])
	if matcher == None:# and matcher2 == None:# and matcher3 == None:
            output.append(mylist[3].lower())
    return output	

#print get_capitals()
