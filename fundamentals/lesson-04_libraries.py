# library time
# i reckon
# yar
# matey

# le math
import math

sq_rt = math.sqrt(144)
print("Square Root:", sq_rt)

up = math.ceil(144)
print("Rounded Up:", up)

down = math.floor(144)
print("Rounded Down:", down)

expo = math.pow(144, 4)
print("To the 4th:", expo)

# constant time!!
# they never change, apparently
# written in all caps

PI = math.pi
print(PI, "\n")

TTQTSBBKLAKKKK = (1, 2, 3, 5) # 4

# Challenge 1: Circle Area with Math Library
# Use two variables "radius" and "circle_area" to calculate the area of a circle with a diameter of 14.

diameter = 14
radius = diameter / 2
circleArea = PI * radius ** 2
print(f'{circleArea} units')


# random
import random

# Create your own pseudorandom number generator that utilizes as seed to output a random number. 
# The seed should be a floating-point number with five total digits (including those before and after the decimal), and it must be greater than 100.0. 
# Perform at least 3 different math calculations on it (ie, addition, subtraction, and division). 
# Use math library to round the float UP to an integer. 
# BONUS CHALLENGE: Make your random number output between 1 and 10.

seed = 97833
mult = seed ** (2 * math.pi) / (seed ** 2)
div = math.cos(seed) + math.sin(seed)
add = 1.002 ** seed
sub = 1.001 ** seed
numberiguess = math.ceil((seed * mult / div + add - sub) % seed)
print(numberiguess)

# idk ts cool too??

for m in range(42):
    if seed % 2 == 1:
        seed = seed * 3 + 1
    else:
        seed = seed / 2
print(seed)
print("\n")

# k now it's actually time for random lib
randint = random.randint(1, 5000)
print(randint)

randflt = random.random()
print(randflt)

list = ["m", "mm", "mmm", "mmmm"]

select = random.choice(list)
print(select)

random.shuffle(list)
print(list)
print("\n")

# Challenge 2: Simulate a Die Roll
# Use the random library to simulate rolling a six-sided die.
# The output should be a random integer between 1 and 6.
# Store the result in a variable called "die_roll" and print it with a message.

die_roll = random.randint(1, 6)
print(die_roll) # i suppose chap
# surely that can't be it

# Challenge 3: Random Square Root
# Use random library to pick a number between 1 and 75. Store it in "num".
# Use math library to find its square root.
# Print the number, its square root, and the square root rounded UP with math.ceil().

num = random.randrange(1, 75)
sqrtnum = math.sqrt(num)
print(math.ceil(sqrtnum))

# Challenge 4: Power Roll
# Roll two dice with the random library: one is the "base", and one is the "exponent".
# Use math library to raise the base to the exponent.
# Print both rolls and the result as an integer.

die1 = random.randint(1, 6)
die2 = random.randint(1, 6)
onetothetwoth = math.pow(die1, die2) # twoth
print(int(onetothetwoth)) # tooth