from bs4 import BeautifulSoup
import os

def create_classoom(letter):
    return os.getcwd() + "/classoom_" + letter + ".html"
    

def check_for_classroom(letter):
    return os.path.exists(create_classoom(letter))

def generate_alphabet():
    return ['A', 'B', 'C', 'D', 'E', 'F'
            , 'G', 'H', 'I', 'J', 'K', 'L'
            , 'M', 'N', 'O', 'P', 'Q', 'R'
            , 'S', 'T', 'U', 'V', 'W', 'X'
            , 'Y', 'Z']

#HTML Parsing.
def make_soup(text):
    return BeautifulSoup(text, 'html.parser')

def make_rows(soup_obj):
    return soup_obj.findAll("tr", { "align" : "right"})

def make_columns(soup_obj):
    return soup_obj.findAll('td')

folder_name = input("Please insert the name of the folder containing the 'classroom' files.")
mapping = {}

if os.path.isdir(folder_name):
    print("Path exists: Continuing to parse classroom HTML")
    os.chdir(folder_name)
    for i in generate_alphabet():
        if check_for_classroom(i):
            mapping[i] = True
        else:
            mapping[i] = False
else:
    print("Sorry, that folder does not exist.")
    exit(1)


LCOM = 0
DIT = 0
IFANIN = 0
CBO = 0
NOC = 0
RFC = 0
NIM = 0
NIV = 0
WMC = 0

for i in mapping.keys():
    if mapping[i] is True:
        with open(create_classoom(i), "r") as file:
            data = file.read()
            current_soup = make_soup(data)
            rows = make_rows(current_soup)
            for i in rows:
                col_counter = 0
                for j in make_columns(i):
                    if col_counter != 0:
                        if col_counter == 1:
                            LCOM += int(j.text)
                        if col_counter == 2:
                            DIT += int(j.text)
                        if col_counter == 3:
                            IFANIN += int(j.text)
                        if col_counter == 4:
                            CBO += int(j.text)
                        if col_counter == 5:
                            NOC += int(j.text)
                        if col_counter == 6:
                            RFC += int(j.text)
                        if col_counter == 7:
                            NIM += int(j.text)
                        if col_counter == 8:
                            NIV += int(j.text)
                        if col_counter == 9:
                            WMC += int(j.text)
                        
                    col_counter = col_counter + 1

    
os.chdir("../")

print(LCOM)
print(DIT)
print(IFANIN)
print(CBO)
print(NOC)
print(RFC)
print(NIM)
print(NIV)
print(WMC)

