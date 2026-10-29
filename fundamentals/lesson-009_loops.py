# loopy loop haha
# they repeat a certain sequence of code until a certain limit
# 2 kinds

import time

# i for my loop until i in

animals = ["lamb", "sheep", "cow", "goose", "donkey"]

print("\nwe got\nuh\n", animals)

print()

for animal in animals:
    print("i wish a gruesome fate, full of anguish and despair, to the", animal)
    time.sleep(1)

print()

# you can loop a specific amount of times using range()

for n in range(5):
    print("ts is number", n)

print()

# range() can actually take several arguements
# range([START], [STOP], [STEP])
# where start is the starting value
# stop is the stopping value (plus anything past that)
# step is the value that is jumped between each iteration

for m in range(0, 257, 4):
    print(m)

print()

# strings can be looped too

word = "condemnation"
letList = []

for letter in word:
    print(letter)
    letList.append("!" + letter + "!")
print(letList)

print()

# Challenge 1: Sum Calculator
# Use a for loop to find the sum of numbers from 1 to 10.
# It'll be like sigma notation, or something.

sum = 0
for b in range(11):
    sum += b
print(sum)

print()

# while loop time
# will loop as long as a givn codnition is true
# if your condition never changes it will most likely run until all resources are exhausted
# not so jolly situation

cnt = 0
while cnt < 231:
    print(f"this is no. {cnt}")
    cnt += 1
    time.sleep(0.005)

print()

userInput = ""
while userInput != "1":
    userInput = input("press 1 please\n")

print()

# with control stf too??

for i in range(11):
    print(i)
    if i == 2:
        print("live 2 reaction")
        continue
    if i == 5:
        pass # placeholder command, nothing happens but it won't produce an error
    if i == 8:
        print("nah")
        break

print()

# Challenge 2: Guess Until Correct
# Create a while-loop that keeps asking for a number until the user types 7.

seven = ""

while seven != "7":
    seven = input("gimme an integer\n")
    if seven != "7":
        print("no likey\n")
    else:
        print("oh my")