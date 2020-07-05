import enchant

dictio = enchant.Dict("en_US")

alph = "abcdefghijklmnopqrstuvwxyz"

file = open("C:/Users/cdobb/AppData/Local/Programs/Python/Python38-32/Lib/site-packages/enchant/data/mingw32/share/enchant/hunspell/en_US.dic")

for line in file:
    if "/" in line:
        line = line[0:(line.index("/"))]
    line = line.lower()
    if len(line) == 5 and "rn" in line:
        temp = ""
        skip = line.index("rn")
        for i in range(0,len(line)):
            if i != skip and i != skip+1:
                temp += line[i]
            if i == skip:
                temp += "m"
        if dictio.check(temp):
            print(line + ", " + temp)

file.close()