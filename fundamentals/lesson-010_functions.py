# also known as methods or procedures for no reason whatsoever
# in the simplest definition, it's kinda just a reusable portion of code but like...
# no retpying everything
# like there's already built-in functions
# idk bro

def spreadNeg():
    print("you are an enemy of christ")
def spreadPos():
    print("one day you'll sit in the sun and things won't feel so bad")

spreadPos() # cal l func
spreadPos()
spreadPos()
spreadPos()
spreadNeg()
# usually, these r supposed to return numbers, not some stupid print() statement

print()

def expressy(n): # the n here would be considered a parameter, a placeholder for an arguement
    return n
expression = expressy(2 + 2) # the expression is an arguement, and will take the place of the parameter in the original definition
print(expression)

print()

def greet(alias):
    return f"what's up, {alias}"
pri = greet("dante")
sec = greet("nero")
ter = greet("virgil")
print(pri)
print(sec)
print(ter)

print()

def remain(a, b):
    return a % b
myRemains = remain(14, expression)
print(myRemains)

print()

def isFar(dis):
    if dis > 1960:
        return "you better drive there"
    if dis <= 1960 and dis >= 460:
        return "you shouldn't just walk there"
    if dis < 460 and dis > 20:
        return "walk"
    if dis <= 20 and dis >= 0:
        return "it's right there"
    if dis < 0:
        return "erm distance can't acutally be negative so uh"
dOne = isFar(2000)
dTwo = isFar(1948)
dThree = isFar(740)
dFour = isFar(12)
print(dOne)
print(dTwo)
print(dThree)
print(dFour)

print()

# I want to create a function that takes in a number and doubles it, then adds it to a list.
# The function should also take in a number of times that we should double the number
# Write a function named doubler() that has TWO parameters: 
# First parameter:  the number i want doubled
# Second paramater: how many times the loop should run 

def doubler(a, b, c):
    for i in range(b):
        a = a * 2
        c.append(a)
list = []
doubler(7, 8, list)
print(list)