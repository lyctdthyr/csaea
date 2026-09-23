import math

print(7 // 2, 7 % 2, -7 // 2)
# obviously the output would just be cos // rounds down, i think
# 3  1  -4

print(int(-5.9), math.floor(-5.9))
# ts would be
# -5  -6
# because int() only murders the float or whatever, but math.floor() properly rounds down

print("5" * 3, "5" + "5")
# 555 55
# because the 5s are quoted so it prints the actual 5 back-to-back

print (2 ** 4, math.pow(2, 4))
# 16  16.0
# math.pow() loves litl float cos yeahh

print(True + True + True)
# idk
# 3
# i guess.
# if True is 1 and False is 0 then it'll work i swear

print(0.1 + 0.2 == 0.3)
# i bet it's NOT gonna be true for some magical reason
# "Surprised? Explain." yeah bud that obviously means it's
# False
# idk why tho ask j vzyz
# "rounding off error"

print("Zebra" < "apple")
# genuinely dunno but i can guess true i suppose
# it's because a tastes better than Z
# a = 97
# Z = 90
# something along those lines

f = False
t = True

print(not f or t and f)
# True
# i guess
# uh i think
# the big pyth evaluates not f as True
# then the big pyth evaluates t and f as False
# n then if you were to print t or f it's True
# bah

nums = [34, 52, 3, 64, 32]

print(nums[-len(nums)])
# the negative length of nums is -5
# it counts backwards 5 numbers, which returns to 34, the first value
# it prints 34 of the array
# i think im bad at this sorry
# ayy im correct im goated

for i in range(10, 0, -3):
    print(i)
# this will of course tell me
# 10
# 7
# 4
# 1
# because the big pyth will subract 3 from 10 until it's below 0

x = 5
while x < 10:
    x += 2
    print(x)
# it's because the very kawaii print() is placed after the x += 2
# so it adds 2 to x before the loop ends once print(x) runs