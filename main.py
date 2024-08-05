"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Doiminik Vícha
email: dominik.vicha@gmail.com
discord: Dominik V #
"""
"""
#ZADÁNÍ:
1. Na úvod si svůj soubor popiš hlavičkou, ať se s tebou můžeme snadněji spojit:
2. Vyžádá si od uživatele přihlašovací jméno a heslo,
3. zjistí, jestli zadané údaje odpovídají někomu z registrovaných uživatelů,
4. pokud je registrovaný, pozdrav jej a umožni mu analyzovat texty,
5. pokud není registrovaný, upozorni jej a ukonči program.**
    5.0 registrovaní uživatelé:
 bob        123     
 ann        pass123   
 mike       password123 
 liz        pass123  
    5.1 Pokud uživatel vybere takové číslo textu, které není v zadání, program jej upozorní a skončí,
    5.2 pokud uživatel zadá jiný vstup než číslo, program jej rovněž upozorní a skončí.
6.Pro vybraný text spočítá následující statistiky:
    6.1 počet slov,
    6.2 počet slov začínajících velkým písmenem,
    6.3 počet slov psaných velkými písmeny,
    6.4 počet slov psaných malými písmeny,
    6.5 počet čísel (ne cifer),
    6.6 sumu všech čísel (ne cifer) v textu.
7. Program zobrazí jednoduchý sloupcový graf, který bude reprezentovat četnost různých délek slov v textu. Například takto:
# ...
 7| * 1
 8| *********** 11
 9| *************** 15
10| ********* 9
11| ********** 10


                        PO SPUŠTĚNÍ BY MĚL PROGRAM VYPADAT:
$ python projekt1.py
username:bob
password:123
----------------------------------------
Welcome to the app, bob
We have 3 texts to be analyzed.
----------------------------------------
Enter a number btw. 1 and 3 to select: 1
----------------------------------------
There are 54 words in the selected text.
There are 12 titlecase words.
There are 1 uppercase words.
There are 38 lowercase words.
There are 3 numeric strings.
The sum of all the numbers 8510
----------------------------------------
LEN|  OCCURENCES  |NR.
----------------------------------------
  1|*             |1
  2|*********     |9
  3|******        |6
  4|***********   |11
  5|************  |12
  6|***           |3
  7|****          |4
  8|*****         |5
  9|*             |1
 10|*             |1
 11|*             |1

                            POKUD UŽIVATEL NENÍ REGISTROVANÝ:
$ python projekt1.py
username:marek
password:123
unregistered user, terminating the program..

"""
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "Liz": "pass123"
}
"""
username = input("Username: ")
password = input("Password: ")

if username in registred_users and registred_users[username] == password:
    print("ok")
else:
    print("not ok")

"""

"""
def check_registration_user(username):

    username = input("Username: ")
    
    if username in registred_users:
            print("ok")
    else:
        print("sorry")
    return(username)

check_registration_user(registred_users)

"""
#print(dir(dict))
#print(help(dict.values))
#print(dict.values(registred_users))

"""
def check_registration_password(password):
     
    password = input("Password: ")

    if password in dict.values(registred_users):
        
        print("ok")
    else:
        print("not ok")
    return(password)

check_registration_password(registred_users)

"""
#ošetřit když je dobre jmeno ale ne heslo (neni ani tak dulezite)
###################POKUD SE STANE ZE DOJDE KE SPATNEMU HESLU, PROGRAM SICE NAPISE ZE USER NENI REGISTROVANY ALE NESKONCI PROGRAM! 

"""
def check_registration(username, password):
# ukonceni programu pres while true? 

    username = input("Enter a username:")
    password = input("Enter a password:")

    if username in registred_users and password in dict.values(registred_users):
        print("Welcome in the app,", username)
    else:
        print("Unregistered user, terminating the program..")
    
    return(username, password)
check_registration(registred_users, dict.values(registred_users))

"""
# DVĚ MOŽNOSTI ŘEŠENÍ 5. -> 1. řešení
"""
try:

    text_number = int(input("Enter a number btw. 1 and 3 to select:"))

    if text_number < 4 and text_number > 0:
        print("----------------------------------------")
    else: 
        print("Warning you selected wrong number.")

except ValueError:
    print("You must select number.")

"""
# MOŽNOST ŘEŠENÍ 5. -> 2. ŘEŠENÍ 

def user_choose_paragraph(TEXTS):
    for index, paragraph in enumerate(TEXTS, start=1):
        print(f"{index}:" , paragraph)
        print("\n-\n")

    question_number = True          # user_choice je urcite lepsi... 
    while question_number:
        text_number = input("Enter a number btw. 1 and 3 to select:")

        if text_number.isnumeric() and int(text_number) in range(1,4):
            print("----------------------------------------")
            break
        else:
            print("Warning you selected wrong number.") 
            break
user_choose_paragraph(TEXTS)

"""
def user_choose_paragraph(TEXTS):
    for index, paragraph in enumerate(TEXTS, start=1):
        print(f"{index}:" , paragraph)
        print("\n-\n")

user_choose_paragraph(TEXTS)


NAPOJIT 5 ČÁST NA VYBRANI TEXTU PŘES FCE
"""











 




    


    
   




