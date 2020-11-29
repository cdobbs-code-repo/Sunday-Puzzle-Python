import enchant

dictio = enchant.Dict("en-US")

def test():
    #animals = ["deer","cow","pig","chicken","dog","cat","lion","hyena","fox", \
    #    "duck","swan","goose","bear","mouse","rat","whale","elk","moose","rabbit"]

    meats = ["beef","chicken","turkey","red","white","dark","pork","bacon","poultry", \
        "fish","lamb","steak"]

    meats = ["ribs"]

    meats = ["veals","hamburger","ham","sausage"]

    meats = ["barbeque","bbq","pepperoni","salami"]

    meats = ["mutton","chops","ground"]

    bar = open("C:/Users/cdobb/Desktop/Python_stuff/sunday_puzzle/11_29_2020/animal_list.txt")
    for line in bar:
        animal = line.strip()
        animal = animal[::-1]
        for i in range(0,len(animal)):
            for meat in meats:
                temp = animal[:i] + meat + animal[i:]
                if dictio.check(temp):
                    print(temp)

def main():
    test()

if __name__ == "__main__":
    main()