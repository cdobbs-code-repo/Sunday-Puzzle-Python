import re
import enchant

dictio = enchant.Dict("en_US")

def get_binary(mystring):
    out = []
    foo = len(mystring)
    num = ""
    for i in range(0,foo):
        num += "0"
    out.append(num)
    while "0" in num:
        num = bin(int(num,2) + 1)[2:]
        while len(num) < foo:
            num = "0" + num
        out.append(num)
    return out

def get_countries():
    output = []
    with open ("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/07_14_2019/countries.csv", "r") as BigFile:
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
        bar.append(x)

#print(bar)

#1. get all binary numbers in strings for length of name
#print(bar[3])
#print(get_binary(bar[3]))
#2. check if 2 real words for 1's part and 0's part for each country

for x in bar:
    tempbin = get_binary(x)
    for bins in tempbin:
        i = 0
        thing1 = ""
        thing2 = ""
        for zerone in bins:
            if zerone == "0":
                thing1 += x[i]
                i+=1
            if zerone == "1":
                thing2 += x[i]
                i+=1
        if thing1 != "" and thing2 != "" and dictio.check(thing1) and dictio.check(thing2):
            print(x + ", " + thing1 + ", " + thing2)