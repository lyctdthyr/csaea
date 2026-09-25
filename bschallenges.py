# "A restaurant bill comes to $50. Calculate a 20% tip and the total, and print both using an f-string. Use math operators and an f-string."
# Given:
bill = 50

# yadayada
print(f"A 20% tip would be ${bill * 0.2} and the total amount being payed would be ${bill * 1.2}. \n")

# "You are ordering pizza for your class. Use the math library to calculate how many whole pizzas to order, then print how many extra slices will be left over. Use the math library and math operators."
# Given:
import math
 
students = 23
slices_per_student = 2
slices_per_pizza = 8

 # i hate this already
print(f"There'd need to be {math.ceil(students * slices_per_student / slices_per_pizza)} pizzas, which would leave {students * slices_per_student % slices_per_pizza} extra slices for me. \n")

# "A weather app gets temperatures in Fahrenheit. Convert to Celsius using C = (F - 32) * 5 / 9 and print the result in a full sentence. Use math operators and an f-string."
# shut up goddamn
# Given:
fahrenheit = 212
 
# huh
celsius = (fahrenheit - 32) * 5 / 9
print(f"This is a full sentence and {fahrenheit} degrees Fahrenheit is {int(celsius)} degrees celsius. \n")

# "Print the letter grade: 90+ is A, 80+ is B, 70+ is C, 60+ is D, anything lower is F. Change the score to test every grade. Use conditionals (if, elif, else) and comparisons."
# fuck
# Given:
score = 84
 
# <Your Code Here>
if score < 60:
    print("F, you suck lmao")
elif 70 > score >= 60:
    print("D, you suck lmao")
elif 80 > score >= 70:
    print("C, you suck lmao")
elif 90 > score >= 80:
    print("B, you suck lmao")
elif 100 > score >= 90:
    print("A, pretty mid twin")
else:
    print("nerd")
print("\n")

# Print "Access granted" if the attempt matches the password exactly, otherwise print "Access denied". The given attempt was typed with Caps Lock on. Use comparisons and conditionals.
# "Access granted" are we deadass
# Given:
password = "csaea2026"
attempt = "CSAEA2026"

# pf
if password == attempt:
    print("Good boy.")
else:
    print("Access denied")
print("\n")

# "On street-sweeping days, cars with even license numbers park on the east side and odd numbers park on the west. Print which side this car should park on. Use the % math operator, comparisons, and conditionals."
# Given:
plate = 4827
 
# <Your Code Here>
print("is it even street-sweepin time? \ni haven't even cried...")
if plate % 2 == 1:
    print("you're supposed to go west, bum.")
else:
    print("you're supposed to go east, bum.")
print("\n")

# "Riders must be at least 48 inches tall. Riders under 10 years old also need an adult with them. Print whether this person may ride. Use logical operators and conditionals."
# Given:
height = 50
age = 8
has_adult = True
 
# <Your Code Here>
if height < 48:
    print("ge tout")
if height >= 48:
    print("aight twin...")
    if age < 10:
        if has_adult == False:
            print("ge tout")
        else:
            print("go")
    else:
        print("go")
print("\n")

# ""
# Given:
first = "Ada"
last = "Lovelace"
school = "CSAEA"
 
# who wants their last name to be lovelace cro
print(first + last + school)
print("just so you know putting your full name in a username is like... \n", "against internetting 101 gng \n")

# "The list holds the prices of the items in a shopping cart. Use a loop to add them up and print the total and the number of items. Use a for loop and len()."
# Given:
cart = [12, 5, 30, 8]
 
# <Your Code Here>
