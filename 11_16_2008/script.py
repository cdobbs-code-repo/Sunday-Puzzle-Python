
def letters_in_both_sequentially(short, longg):
    total = len(short)
    count = 0
    for lett in longg:
        if count == total:
            return True
        if short[count] == lett:
            count += 1
    if count == total:
        return True
    return False
        



foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_16_2008/authors_last_name_C.txt")

last_name_list = []
for names in foo:
    names = names.split("(")[0]
    names = names.strip()
    last_name = names.split(" ")[-1]
    last_name_list.append(last_name)
foo.close()

for long_name in last_name_list:
    for short_name in last_name_list:
        if len(short_name) == len(long_name) - 4:
            if letters_in_both_sequentially(short_name,long_name):
                print(short_name)
                print(long_name)
                print("------------------")


# Cervantes
# Crane