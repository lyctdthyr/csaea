# yeah yeah math operators i get it cro
# + - * / // % **

# import math
# oh wait

add = 1411 + 4574
print("Sum:", add)

sub = 15677 - 9183
print("Dif:", sub)

mult = 86 * 32
print("Prod:", mult)

flt_div = 73 / 12
print("Quot:", flt_div)
# / spits up a float

int_div = 73 // 12
print("Quot:", int_div)
# // ignores the remainder after it divides

mod = 73 % 12
print("R:", mod)
# % ignores everything it just divided and spits up the remainder

exp = 73 ** 12
print("Exp:", exp)

# did you know?
# python loves pemdas
# yes
# the order math operations are supposed to performed to successfully "solve" a complex equation
# how wonderful

scary = (34 ** 2 + 17) * 2
print("Tot:", scary)

scary0 = 2 ** 3 * 4
print("Tot:", scary0)

scary1 = 5 + 2 ** 3 * (4 - 1)
print("Tot:", scary1)


# Challenge 1: Rectangle Area
# Calculate the area of a rectangle with a width of 8 and a height of 5.
# Create separate variables for width, height, and result. Print result.

wide = 8
high = 5
area = wide * high
print(f'\n{area} units')

# Challenge 2: Circle Area
# Use the formula πr² to calculate the area of a circle with radius 7.

import math

radius = 7
area0 = math.pi * radius ** 2
print(f'{area0} units')

# crap
# deport math
# i guess

pi = 3.14
radius0 = 7
area1 = 3.14 * radius0 ** 2
print(f'{area1} units')

# Challenge 3: Shopping Total
# A book costs $12.99 and a notebook costs $3.50.
# Calculate the total cost for 3 books and 4 notebooks.

talecost = 12.99
notecost = 3.50
tales = 3
notes = 4
taxratelol = 1.06625
print(f'\nBook Cost: ${talecost}\nNotebook Cost: ${notecost}\nTotal: ${((tales * talecost + notes * notecost) * taxratelol):.2f}\n')

# Challenge 4: Even or Odd
# Use the modulus operator to check if the number 57 is even or odd.
# Bonus: use a conditional to print "Even" if it is even, and "Odd" if it is odd.

variablewhichmayormaynotbefiftyseven = 57
if variablewhichmayormaynotbefiftyseven % 2 == True:
    print("odd")
else:
    print("even")
# chat, is my writing fire?