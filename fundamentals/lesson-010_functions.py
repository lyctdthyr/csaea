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
dThree = isFar(340)
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

def doubler(number, iterations):
    list = []
    a = number
    for i in range(iterations):
        a *= 2
        list.append(a)
    return list
liste = doubler(7, 8)
print(liste)

print()

# Challenge 1. 
# Make a calculator with 4 procedures that accept two arguments each.
# 1) add any two numbers and print the result
# 2) subtract any two numbers and print the result
# 3) divide any two numbers and print the result
# 4) multiply any two numbers and print the result

def addts(a, b):
    return a + b
def subts(a, b):
    return a - b
def multts(a, b):
    return a * b
def divts(a, b):
    return a / b
sum = addts(2, 3)
dif = subts(2, 3)
prod = multts(2, 3)
quot = divts(2, 3)
print(sum)
print(dif)
print(prod)
print(quot)

print()

# Challenge 2
# Make a function called average that:
# 1) accepts five numbers
# 2) returns the average
# 3) print the returned value outside the function

def mean(*args):
    a = 0
    for i in args:
        a += i
    a /= len(args)
    return a
average = mean(4, 5, 6, 9, 10, 76, 3, 1, 0, 0, 4, 8)
print(average)

print()

# Challenge 3
# Make a function called is_even that:
# 1) accepts one number
# 2) prints "Even" if the number is even
# 3) prints "Odd" if the number is odd

def evenodd(number): # i don't like the name is_even, hope this works
    mod = number % 2
    if mod == 1:
        return "odd"
    elif mod == 0:
        return "even"
    else:
        raise TypeError("number must be an integer") # what was he cooking?
even = evenodd(89)
odd = evenodd(24)
error = evenodd(180)
print(even)
print(odd)
print(error)

print()

# Challenge 4
# Make a function called "analyze_word" that counts how many vowels and consonants are in a word
# Call the function with a sample one-word string and print the returned result outside the function

def analyze_word(word):
    consCt = 0
    vowCt = 0
    if isinstance(word, str) == False:
        raise TypeError("word must be a string")
    elif word.isalpha() == False:
        raise ValueError("word must only contain alphabetical characters")
    else:
        for let in word:
            if let in "aeiou":
                vowCt += 1
            else:
                consCt += 1
    return [vowCt, consCt, consCt + vowCt]
fahhh = analyze_word("antidisestablishmentarianism")
print(fahhh)