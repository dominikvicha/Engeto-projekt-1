'''
author =
'''
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

#ZKOUŠKA A
"""
username = input("Username: ")
password = input("Password: ")

if username in registred_users and registred_users[username] == password:
    print("ok")
else:
    print("not ok")

"""
#ZKOUŠKA B
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

#ZKOŠUKA 3
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


# MOŽNOST ŘEŠENÍ 5. -> 2. ŘEŠENÍ 

"""
 user_choice = True         
    while user_choice:
        user_choice = input("Enter a number btw. 1 and 3 to select:")

        if user_choice.isnumeric() and int(user_choice) in range(1,4):
            print("----------------------------------------")
            break
        else:
            print("Warning you selected wrong number.") 
            break
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
"""
def choose_paragraph(texts):
    # Display the available paragraphs
    for i, text in enumerate(texts, start=1):
        print(f"Paragraph {i}:")
        print(text)
        print("\n---\n")
    
    # Prompt the user to select a paragraph
    try:
        choice = int(input("Please choose a paragraph (1-3): "))
        if 1 <= choice <= len(texts):
            print(f"\nYou chose Paragraph {choice}:")
            print(texts[choice - 1])
        else:
            print("Invalid choice. Please choose a number between 1 and 3.")
    except ValueError:
        print("Invalid input. Please enter a number.")

# Run the function to allow user interaction
choose_paragraph(TEXTS)
"""
"""
Understanding texts[choice - 1]
1. List Indexing in Python:

Python lists are zero-indexed, which means the first element of a list has an index of 0, the second element has an index of 1, and so on.
The texts list in this case contains three paragraphs, which means they are stored at indices 0, 1, and 2 respectively.

2. User Input and Human Readability:
When displaying options to the user, it's common practice to start numbering from 1, as it aligns with natural human counting and is more intuitive.
Therefore, when the user is prompted to choose a paragraph, they are asked to select between 1, 2, and 3.

3. Adjustment for Zero-Indexed List:
Since the user chooses numbers 1, 2, or 3 but the list indices are 0, 1, and 2, we need to adjust the user's choice to match the correct index in the list.
Subtracting 1 from the user's choice (choice - 1) aligns the user's selection with the correct index in the list. For example:
If the user selects 1, choice - 1 becomes 0, which corresponds to the first paragraph (texts[0]).
If the user selects 2, choice - 1 becomes 1, corresponding to the second paragraph (texts[1]).
If the user selects 3, choice - 1 becomes 2, corresponding to the third paragraph (texts[2]).

4. Displaying the Selected Paragraph:
texts[choice - 1] accesses the paragraph from the list based on the adjusted index.
print(texts[choice - 1]) outputs the content of the selected paragraph to the console.

Summary
The use of print(texts[choice - 1]) is a necessary adjustment to account for the difference between user-friendly numbering (starting at 1) and Python's list indexing (starting at 0). This ensures that when a user selects a paragraph, the corresponding text from the list is correctly displayed.

"""


#print(dir(TEXTS))
# There are 54 words in the selected text.

# Given paragraph
paragraph1 = '''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley.
'''

# Step 1: Split the paragraph into words
words = paragraph1.split()

# Step 2: Initialize counters and sum
titlecase_count = 0
numeric_strings_count = 0
sum_of_numbers = 0

# Step 3: Iterate through each word
for word in words:
    # Remove punctuation from the word
    stripped_word = word.strip(",.")
    
    # Check if the word is titlecase
    if stripped_word.istitle():
        titlecase_count += 1
    
    # Check if the word is numeric
    if stripped_word.isdigit():
        numeric_strings_count += 1
        sum_of_numbers += int(stripped_word)

# Step 4: Print the results
print(f"Titlecase words count: {titlecase_count}")
print(f"Numeric strings count: {numeric_strings_count}")
print(f"Sum of all numbers: {sum_of_numbers}")


    