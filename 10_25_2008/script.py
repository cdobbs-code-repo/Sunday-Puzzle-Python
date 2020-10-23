import time

def remove_spaces(foo):
    output = ""
    for each in foo:
        if each != " ":
            output += each
    return output

def letter_count(word,letter):
    count = 0
    for each in word:
        if each == letter:
            count += 1
    return count


start_time = time.time()

myfile = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/10_25_2008/list_of_us_teams.txt")

for team in myfile:
    starting_word = team

    # preprocess: remove spaces and change all letters to lowercase
    myword = starting_word.lower()
    myword = myword.strip()
    myword = remove_spaces(myword)

    # get set of letters
    letter_set = set(myword)

    # skip if main criteria not met (8 unique letters, 20 total letters)
    if len(myword) == 20 and len(letter_set) == 8:
        # get dictionary with letter set and count of letters in word
        mydict = {}
        for lett in letter_set:
            mydict.update({lett:letter_count(myword,lett)})


        # print(mydict)
        # print(mydict.values())

        one_count = 0
        two_count = 0
        three_count = 0
        four_count = 0
        higher_count = 0

        for counts in mydict.values():
            if counts == 1:
                one_count += 1
            elif counts == 2:
                two_count += 1
            elif counts == 3:
                three_count += 1
            elif counts == 4:
                four_count += 1
            else:
                higher_count += 1

        if one_count == 2 and two_count == 2 and three_count == 2 \
            and four_count == 2 and higher_count == 0:
            print(starting_word)

print("Program run time (seconds): " + str(time.time() - start_time))
