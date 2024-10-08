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

registered_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "Liz": "pass123"
}

def check_registration():

    username = input("Enter a username:")
    password = input("Enter a password:")

    if username in registered_users and password == registered_users.get(username):
        print(f"\nWelcome in the app,", username)
        print(f"\nWe have 3 texts to be analyzed.") 
    else:
        print("Unregistered user, terminating the program..")
        exit()
    

def user_choose_paragraph():

    try: 
        user_choice = int(input("Enter a number btw. 1 and 3 to select:"))
        if not 1 <= user_choice <= len(TEXTS):
            raise ValueError("You selected wrong number.")
        
    except ValueError as e:
        print(e)
        exit()
   
    return user_choice


def stats_count(paragraph):

    word_count = 0
    titlecase_count = 0
    uppercase_count = 0
    lowercase_count = 0
    numeric_string = 0
    sum_numbers = 0

    word_frequency = {}
    paragraph = paragraph.replace("-", " ")
    words = paragraph.split()
    symbols = ("().,?!-%*/")

    stripped_words = [(word.strip(symbols)) for word in words]

    for word in stripped_words: 

        if word.__len__():
            word_count += 1

        if word.istitle():
            titlecase_count += 1

        if word.isupper() and word.isalpha():
            uppercase_count += 1

        if word.islower():
            lowercase_count += 1
        
        if word.isdigit():
            numeric_string += 1
            sum_numbers += int(word)

        if word in word_frequency:
            word_frequency[word] += 1
        else:
            word_frequency[word] = 1
    print(stripped_words)

    print(f"Words: {word_count}")
    print(f"Titlecase words: {titlecase_count}")
    print(f"Upercase words: {uppercase_count}")
    print(f"Lowercase: {lowercase_count}")
    print(f"Numeric srings: {numeric_string}")
    print(f"Sum of all numbers: {sum_numbers}")
    print("-" * 35)

    return stripped_words

def graph(words):
    print(f"{'LEN':<5}|{'OCCURRENCES':^20}|{'NR.':<5}")
    print("-" * 35)

    for i in range(1, 20):
        stats = 0 
        for word in words:
            if len(word) == i:
                stats += 1
        graph_stats = str(stats * "*")
        print(f"{i:<5}|{str(graph_stats):<{20}}|{stats}")

def main():
    check_registration()
    paragraph = TEXTS[user_choose_paragraph() - 1]
    words = stats_count(paragraph)
    graph(words)

if __name__ == "__main__":
    main()







    






        















