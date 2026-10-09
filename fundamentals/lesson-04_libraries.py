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

seed = 16.971
mult = seed ** (2 * math.pi) / (seed ** 2)
div = math.cos(seed) + math.sin(seed)
add = 5 ** seed + 3 * seed
sub = 6 ** seed - 2 * seed
numberiguess = math.ceil(seed * mult / div + add - sub)
print(numberiguess)