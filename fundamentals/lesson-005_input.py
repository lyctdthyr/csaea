# computah
# usah input time

name = input("give me your name.\n")
print(f'hi {name}.')
age = input("how old are you twin? like in years? human ones? integer only? or else i die?y\n")
# input always stores things as a string
# for no reason at all
age = int(age)
print(f"i highly doubt that you're {age} yrs old but alright")
height = float(input("now, tell me how tall you are. in meters.\n"))
print(f"{height} meters?\nshorty.")

# Challenge 1: Favorite Color
# Ask the user for their favorite color and print out a message using it.

color = input("what's your favorite color?\n")
print(f"{color} is mid lmao.\nge tout")

# Challenge 2: Adding Two Numbers
# Ask the user for two numbers, add them together, and print the result.

num1 = int(input("now gimme a number:\n"))
num2 = int(input("now gimme another one:\n"))
print(f"{num1 + num2}. im so cool")

# Challenge 3: Circle Area from User Input
# Ask the user for the diameter of a circle, then calculate and print the area.
# pi radius squared 

import math
print("you like circles? me too.")
diameter = int(input("tell me, how many units should the diameter be?\n"))
radius = diameter / 2
print(f"your circle is about {math.pi * radius ** 2} square units large")

# Challenge 4: Custom Die Roll
# Ask the user to enter how many sides the die should have.
# Then simulate rolling the die once and print the result.

import random
print("you like dice? me too.")
die = int(input("tell me, how many sides should a die have?\n"))
print(f"i got...\n{random.randint(1, die)}\nnice?")