
import enchant

diction = enchant.Dict("en-US")

def get_list_of_backwards_animals() -> list:
    mylist = []
    bar = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/animal_list.txt")
    for line in bar:
        animal = line.strip()
        animal = animal[::-1]
        mylist.append(animal)
    return mylist

##
## SET list of backwards animals GLOBALLY
##

backwards_animal_list = get_list_of_backwards_animals()

def split_foo_in_bar(foo: str,bar: str) -> bool:
    # Example - foo = "ANIMAL":
    # bar = A-...-NIMAL # TRUE
    # bar = AN-...-IMAL # TRUE
    # bar = ANI-...-MAL # TRUE
    # bar = ANIM-...-AL # TRUE
    # bar = ANIMA-...-L # TRUE
    if len(bar) <= len(foo):
        return False
    for i in range(1,len(foo)-1):
        temp = bar[:i] + bar[-(len(foo)-i):]
        if temp == foo:
            return True
    return False

def SPLIT_backwards_animal_in_bar(bar: str) -> bool:
    for animal in backwards_animal_list:
        if split_foo_in_bar(animal,bar):
            return True
    return False

def get_list_of_words_with_SPLIT_backwards_animals_in_them():
    foo = open("C:/Python39/Lib/site-packages/enchant/data/mingw64/share/enchant/hunspell/en_US.dic")
    output = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/backwards_animal_in_word_list.txt","w")
    for bar in foo:
        bar = bar.strip().split("/")[0]
        bar = bar.lower()
        if SPLIT_backwards_animal_in_bar(bar):
            output.write(bar+"\n")
    foo.close()
    output.close()


def get_meat_list() -> list:
    meats = []
    foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/meat_list.txt")
    for bar in foo:
        meats.append(bar.strip())
    foo.close()
    return meats

def look_for_meat_variety_in_animal_word_list():
    # meat_list = ["beef","chicken","turkey","red","white","dark","pork","bacon","poultry", \
    #     "fish","lamb","steak","ribs","veals","hamburger","ham","sausage","barbeque","bbq",\
    #         "pepperoni","salami","mutton","chops","ground"]
    meat_list = get_meat_list()
    animal_list = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/animal_list.txt")
    for animal in animal_list:
        animal = animal.strip()
        animal = animal[::-1]
        for meat in meat_list:
            for i in range(1,len(animal)-1):
                temp = animal[:i] + meat + animal[i:]
                if diction.check(temp):
                    print(temp + " - " + meat + "-" + animal)

#-----------------------------------------------------------
def main():
    # get_list_of_words_with_SPLIT_backwards_animals_in_them() # stored in text file ONLY RUN THIS IF ALGORITHM CHANGES
                                                               # and only run it ONCE.
    look_for_meat_variety_in_animal_word_list()



#-----------------------------------------------------------
if __name__ == "__main__":
    main()
