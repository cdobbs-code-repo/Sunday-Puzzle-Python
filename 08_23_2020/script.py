import enchant

#--------------function-junction----------------------------
# get all binary numbers with three ones and enough zeros such that 3 + #{zeros} = #{word characters}
# Note: this is so we can iterate through all possible combinations of incrementing 3 characters easily
# [see associated weekly puzzle explanation for further explanation]

# INPUTS:  integer > 3
# OUTPUT:  list of all binary numbers meeting above criteria 

def get_binary_threes(leng):
    # initialize output array
    myout = []
    # get maximum number to set iteration max. This number will be
    # in binary 1110...0 (or 1110 if leng = 4)
    maxi = 2**(leng-1) + 2**(leng-2) + 2**(leng-3) + 1
    for i in range(0, maxi):
        # get binary representation
        foo = bin(i)
        # splice off '0b' 
        foo = foo[2:]
        # pad with zeros to maintain desired number size
        while len(foo) < leng:
            foo = "0"+foo
        count = 0
        # count 1s in binary number
        for each in foo:
            if each == "1":
                count += 1
        # if number of 1s is three we add it to the output list
        if count == 3:
            myout.append(foo)
    return myout
#---------------------------------------------------------

#--------globals------------------
dictio = enchant.Dict("en_US")
alph = "abcdefghijklmnopqrstuvwxyza"
nums = "0123456789"
file = open("C:/Users/xxxx/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")
#---------------------------------

for line in file:
    # remove all extra characters and flag non alphabetical characters - START
    if "/" in line:
        line = line[0:(line.index("/"))]
    line = line.lower()
    if "\n" in line:
        line = line[0:(line.index("\n"))]
    letts = True
    for lett in line:
        if lett not in alph:
            letts = False
    numbers = False
    for each in nums:
        if each in line:
            numbers = True
    # remove all extra characters and flag non alphabetical characters - END

    # if no number, all letters, and word length above 3 continue
    if not numbers and letts and len(line) > 3:
        # get all binary numbers with three ones and enough zeros such that 3 + #{zeros} = #{word characters}
        # Note: this is so we can iterate through all possible combinations of incrementing 3 characters easily
        # [see associated weekly puzzle explanation for further explanation]
        bar = get_binary_threes(len(line))
        for each in bar:
            temp = line
            count = 0
            for num in each:
                if num == "1":
                    try:
                        temp = temp[0:count] + alph[alph.index(temp[count])+1]
                    except:
                        # this just allows me to easily set a debug breakpoint if needed
                        print("breakpoint")
                    if len(temp) < len(line):
                        temp = temp + line[count+1:]
                count += 1
            # if new word in dictionary then print "[word], [new_word]"
            if dictio.check(temp):
                print(line + ", " + temp)

file.close()
