
#sunday puzzle: 09_27_2020

def criteria_met(rest,city):
    city = city[::-1]
    city = city.lower()
    rest = rest.lower()
    count = 0
    for i in range(0, len(rest)):
        if rest[i] == city[i]:
            count += 1
    if count == len(rest)-1:
        return True
    else:
        return False

file1 = open('C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/09_27_2020/list_of_cities.txt')

for city in file1:
    city = city.strip()
    for i in range(0,len(city)):
        temp = city[::-1]
        file2 = open('C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/09_27_2020/list_of_restaurant_chains_US.txt')
        for rest in file2:
            rest = rest.strip()
            if len(rest) == len(city):
                if criteria_met(rest,city):
                    print(rest)
                    print(city)
        file2.close()

        
