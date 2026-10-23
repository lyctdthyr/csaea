# lists
# i know a list
# ts ordered, mutable, and uhh
# permit the existence of malignant, vile, horrible skinwalkers

mtList = []
animTuff = ["monkey", "boar", "human", "bear", "fox", "spider", "rooster"]
numList = [1, 4, 90, 87, 90, 12]
nutMix = [True, 5, "wow", False]

print("Animals list:", animTuff)
print("Numbers list:", numList)
print("Mixed data types list", nutMix)

print()

# print the third element in animals
print(animTuff[2])

print()

# print the last element in numbers
print(numList[-1])

print()

#print the first element in the mixed list
print(nutMix[0])

print()

# reassign, append, insert, idk i guess
animTuff[-1] = "worst boss fight oat"
print(animTuff)

animTuff.append("stone monkey")
print(animTuff)

animTuff.insert(3, "dragon")
print(animTuff)
animTuff.insert(6, "scorpion")

# removal
animTuff.remove("dragon")
print(animTuff)

# pop
meh = animTuff.pop()
print(meh)
print(animTuff)

print("\n")

# Challenge 1: Number Swap
# Store this list in a variable: [1, 2, 3, 4, 5, 6] 
# Ask the user to enter a new integer
# Replace the third integer in the original list with the user’s input, and then print the updated list

aList = [1, 2, 3, 4, 5, 6]
print(aList)
inte = input("gimme a number\npreferably and integer\n")
inte = int(inte)
aList[2] = inte
print(aList)

print()

# Challenge 2: Shopping List Manager
# Initialize an empty list called "shopping"
# Add three items of your choice using .append()
# Then insert one extra item at the second position and remove one item of your choice
# Finally, print the final shopping list

shopping = []
shopping.append("pringles tube")
shopping.append("sponges")
shopping.append("banana")
shopping.insert(1, "pokemon cards")
print(shopping)

print("\n")

# ayy
bums = [6, 8, 2, 33, 67, 10, 890, 1, 3, 52, 4.98]
print("numbers: ", bums)

print("Length: ", len(bums))
print("Low: ", min(bums))
print("High: ", max(bums))
print("Sum: ", sum(bums))

bums.sort()
print(bums)

print()

animTuff.sort()
print(animTuff)

print()

bums.reverse()
print(bums)

print()

# woah i can use if statements and lists together??
if "monkey" in animTuff:
    print("destined one omg")
else:
    print("random kid\nge tout")

print("\n")

# Challenge 3: Number Stats
# Create a list of five floats called measurements.
# Print the length, minimum, maximum, and sum of the list using built-in functions.

msrs = [3.44, 98.12, 6.0, 8231.458, 2.701]
print(len(msrs))
print(min(msrs))
print(max(msrs))
print(sum(msrs))