import enchant

def only_letters(word):
    alphi = "abcdefghijklmnopqrstuvwxyz"
    for x in word:
        if x not in alphi:
            return False
    return True

mydict = enchant.Dict("en-US")

foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/10_18_2020/list_of_capitals.txt")

for bar in foo:
    bar = bar.lower()[:-1]
    if only_letters(bar):
        for i in range(1,len(bar)-1):
            temp1 = bar[:i] + "d"
            temp2 = "y" + bar[i+1:]
            temp3 = temp1 + temp2
            for x in range(2,len(temp3)-1):
                temp1 = temp3[:x]
                temp2 = temp3[x:]
                if mydict.check(temp1):
                    if mydict.check(temp2):
                        print(bar)
                        print(temp1)
                        print(temp2)
                        print("-----------------------")
