import requests
import re

# globals
state_list = ["Alabama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa","Kansas","Kentucky","Louisiana","Maine","Maryland","Massachusetts","Michigan","Minnesota","Mississippi","Missouri","Montana","Nebraska","Nevada","New Hampshire","New Jersey","New Mexico","New York","North Carolina","North Dakota","Ohio","Oklahoma","Oregon","Pennsylvania","Rhode Island","South Carolina","South Dakota","Tennessee","Texas","Utah","Vermont","Virginia","Washington","West Virginia","Wisconsin","Wyoming"]
element_list = ["Hydrogen","Helium","Lithium","Beryllium","Boron","Carbon","Nitrogen","Oxygen","Fluorine","Neon","Sodium","Magnesium","Aluminium","Silicon","Phosphorus","Sulfur","Chlorine","Argon","Potassium","Calcium","Scandium","Titanium","Vanadium","Chromium","Manganese","Iron","Cobalt","Nickel","Copper","Zinc","Gallium","Germanium","Arsenic","Selenium","Bromine","Krypton","Rubidium","Strontium","Yttrium","Zirconium","Niobium","Molybdenum","Technetium","Ruthenium","Rhodium","Palladium","Silver","Cadmium","Indium","Tin","Antimony","Tellurium","Iodine","Xenon","Caesium","Barium","Lanthanum","Cerium","Praseodymium","Neodymium","Promethium","Samarium","Europium","Gadolinium","Terbium","Dysprosium","Holmium","Erbium","Thulium","Ytterbium","Lutetium","Hafnium","Tantalum","Tungsten","Rhenium","Osmium","Iridium","Platinum","Gold","Mercury","Thallium","Lead","Bismuth","Polonium","Astatine","Radon","Francium","Radium","Actinium","Thorium","Protactinium","Uranium","Neptunium","Plutonium","Americium","Curium","Berkelium","Californium","Einsteinium","Fermium","Mendelevium","Nobelium","Lawrencium","Rutherfordium","Dubnium","Seaborgium","Bohrium","Hassium","Meitnerium","Darmstadtium","Roentgenium","Copernicium","Nihonium","Flerovium","Moscovium","Livermorium","Tennessine","Oganesson"]
alphabet = "abcdefghijklmnopqrstuvwxyz"

def find_six_three_us_landmark():
    for mysearch in state_list:
        temp_url="http://en.wikipedia.org/wiki/List_of_National_Historic_Landmarks_in_"+mysearch
        r = requests.get(temp_url)
        if str(r) != "<Response [404]>":
            temp_file = str(r.content)
            temp = temp_file.split("title=")
            for line in temp:
                if line[11] == '"' and line[7] == " ":
                    print(line[1:11])

# code above found --> Hoover Dam

def letters_are_in_states(state1: str, state2: str, monument: str, elem: str) -> bool:
    # first do the string sizes make sense
    if len(state1) + len(state2) == len(monument) + len(elem) or len(state1) + len(state2) - 1 == len(monument) + len(elem):
        for letter in monument+elem:
            if letter in state1 or letter in state2:
                pass
            else:
                return False
        return True
    else:
        return False

def get_possible_answers():
    # NOW "hoover dam" + [some element] = [two states]
    for state1 in state_list:
        for state2 in state_list:
            for elem in element_list:
                if letters_are_in_states(state1.lower(),state2.lower(),"hooverdam",elem.lower()):
                    print(state1 + " " + state2 + " " + elem)

def main():
    get_possible_answers()


if __name__ == "__main__":
    main()

