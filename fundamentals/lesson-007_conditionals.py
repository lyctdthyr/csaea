# condhtional thyme
# comparison type shi
# and or not
# if statements

# ufhg we gotta run booleans back
# always capitalized
# mhm
# yes
print(3 == 2)
print(2 == 2)
print("goon" == "edge")
print(1 != 2)
print(4 < 2)
print(1.999 < 2)

print()

# i-i-i-i-i-if

num = 13
if num == 13:
    print(f"{num} is equal to {num} wow")
    print(f"num + num is {num * 2} wow")
# only runs when that little comparison at the top is true
# we know vro

# if and uh
# else

number = 89
if number != 4:
    print("your number is highkey not 4\nbum.")
else:
    print("nice number bro")

print()

# if
# el +
# if uh
# else

temp = 26
if temp >= 25:
    print("pretty warm")
elif 15 < temp <= 24:
    print("pretty meh")
else:
    print("pretty cold")

print()

x = 6
y = 8
if x == y:
    print("x = y")
elif x > y:
    print("x > y")
elif x < y:
    print("x < y")
else:
    print("what")

print()

# and and

age = 16
hasAuth = True
if age >= 16 and hasAuth == True:
    print("yes drive")
else:
    print("no drive")

print()

# and or
# and not

day = "TUES"
if day == "SAT" or day == "SUN":
    print("weekend :)")
else:
    print("survival is a chore\nall perish anyway\nwhy try")

print()

# "is not", i guess

if day is not "TUES":
    print("t hky nt tsdy") # a b c d e f g
else:
    print("t khy s tsdy")

print()

# Challenge 1: Movie Admission
# Ask the user for their age. 
# If under 13, "You can watch PG or G movies."
# If 13–17, “You can watch PG-13 movies.”
# If 18+, “You can watch any movie.”

userAge = input("twin, how old are you?\nlike in human years.\n")
userAge = int(userAge)
if userAge < 13:
    print("you can only watch pg and g rated films bud")
elif userAge <= 17:
    print("you can watch pg-13 rated films and anything rated lighter")
else:
    print("watch whatever")

print()

# Challenge 2: Leap Year
# Rules:
#  - Years divisible by 4 are leap years
#  - unless they're divisible by 100, then they're NOT leap years
#  - unless they're also divisible by 400, then they ARE leap years

year = 1984
if year % 100 == 0 and year % 400 != 0:
    print("not")
elif year % 4 == 0:
    print("leap")
else:
    print("not")