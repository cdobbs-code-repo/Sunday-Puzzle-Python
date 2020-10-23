 
foo = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_08_2008/list_of_capitals.txt")
capitals = foo.read()
foo.close()
capitals = capitals.split("\n")
capitals_list = []
for x in capitals:
    capitals_list.append(x.lower())
    

bar = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_08_2008/animal_list.txt")
animals = bar.read()
bar.close()
animals = animals.split("\n")

for thing_one in animals:
    for thing_two in animals:
        if thing_one[:2] + thing_one[3:] + thing_two[:2] + thing_two[3:] in capitals_list:
            print(thing_one[:2] + thing_one[3:] + thing_two[:2] + thing_two[3:])
            print(thing_one)
            print(thing_two)
            print("--------------------------")


