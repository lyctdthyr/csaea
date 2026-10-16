# i am a tuff manipulator
# of strings or smth
# built-in methods r len() upper() lower() and uh
# capitalize()

greeting = "salutations"
lastName = "vazzy"
# A:
print(greeting, lastName)
# B:
print(greeting + " " + lastName)
# C:
print(f"{greeting} {lastName}")

# numbering starts from 0
# 0 1 2 3 4
# s e v e n

greeting = "salutations" # btw, nothing changed
secondLetter = greeting[1]
print(secondLetter)

# indeingx n slcingn time

newWord = "antidisestablishmentarianism"
print("\nword is like:", newWord)
print("first letter is:", newWord[0])
print("last letter is:", newWord[-1])
print("weird chunk from the middle:", newWord[12:27])
# notice how it includes newWord[12] but not newWord[27]
print("first few letters:", newWord[:8])
print("everything after the first 9 letters:", newWord[8:])
print("last seven letters:", newWord[-7:])
print("every second character:", newWord[1::2])
print("reverse reverse:", newWord[::-1])

lastName = "    Lovelace"
length = len(lastName)
print(f"\n{lastName}")
print(f"ts is apparently {length} characters long\n")

# Challenge 1: Favorite Quote
# Ask the user for their favorite quote and display its length.

quote = input("yo gimme a quote you like, kinda like or something\n")
print(f"your quote has {len(quote)} characters\nshorty.")

# Ask the user to enter a word that is at least 7 characters long. 
# Print the 2nd through 6th characters.
# Use string slicing.

userWord = input('gimme a "word" that has at least 7 characters\n')
if len(userWord) < 7:
    print("i wish you a horrible and gruesome fate")
else:
    userWord = userWord.replace(" ", "")
    if len(userWord) < 7:
        print("i wish you a horrible and gruesome fate")
    else:
        print(f"the second through sixth characters are: {userWord[2:7]}\nyou're welcome")
print("\n")

# Challenge 3: Name Formatter
# Ask the user for their first and last name, then format it as "Last, First".
# Use concatenation or f-strings.

nameUno = input("forename, bro:\n")
nameDos = input("surname, twin:\n")
print(f'ah; "{nameDos}, {nameUno}"? hello')