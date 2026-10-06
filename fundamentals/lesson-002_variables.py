# variables store any form of information
# oftentimes it's better to have somewhat descriptive variable names
# variables may be overwritten

a = 72
print(a)
a = 71
print(a)

password = "password0"
email = "email@gmail.com"
print("Password:\t", password, "\nEmail:\t\t", email)

# boolean naming conventions
isTuff = False
isComplete = False
isEnabled = False

# math conventions
x = 88.35645555
y = 3
print(x + y)

# variables are very flexible
# creating and updating them is highkey easy
t = 15
print(t)
t_down = t - 1
print(t_down)
t = t_down
print(t)
t = t + t
print(t, "\n")

# Challenge 1: Rename Variables
# Change the variable names x, y, z below to more descriptive names

name = "Radia Perlman"
worstnumber = 34
employment = "Networking Engineer"

# Challenge 2: Update Variables
# Create a variable called 'count' with a value of 10
# Use another variable to increase 'count' by 5
# Print the result

count = 10
count_up = count + 5
count = count_up
print(count)

# Challenge 3: Swap Variables
# Given variables x = 4 and y = "hello"
# Swap the values so that x = "hello" and y = 4
# Use a temporary variable. 

x = 4
y = "hello"
temp = 0

temp = x
x = y
y = temp
print(f'\n{x}\t{y}')