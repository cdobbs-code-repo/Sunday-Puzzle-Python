
import enchant

diction = enchant.Dict("en-US")


def get_meat_list() -> list:
    meats = []
    foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/meat_list.txt")
    for bar in foo:
        meats.append(bar.strip())
    foo.close()
    return meats

def get_animal_list() -> list:
    animals = []
    foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/animal_list.txt")
    for bar in foo:
        animals.append(bar.strip())
    foo.close()
    return animals

def look_for_meat_variety_in_animal_word_list():
    meat_list = get_meat_list() # get the list of meats
    animal_list = get_animal_list() # open animal list file
    for animal in animal_list: # for every animal in the animal list
        animal = animal[::-1] # flip the word backwards per the puzzle instructions
        for meat in meat_list: # now we check each animal in our animal list against each meat in our meat list
            for i in range(1,len(animal)-1): # checking for each possible combination of "surrounding" letters
                temp = animal[:i] + meat + animal[i:] # whether the surrounding word is the backwards animal with the meat inside
                if diction.check(temp): # and the amalgamated word will be in common use. 
                    print(temp + " - " + meat + " - " + animal)  # Print the answer when found.

#-----------------------------------------------------------
def main():
    look_for_meat_variety_in_animal_word_list()



#-----------------------------------------------------------
if __name__ == "__main__":
    main()
