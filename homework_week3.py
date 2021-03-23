# EXERCISE 3.1
# For a given word, print it in squares.
# If word = "Python", them the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
print("EXERCISE 3.1:")
word = "Martyna"
frame = "---"
list_of_char = tuple(word)
word_length = len(list_of_char)
for x in range(word_length):
    print("+{}".format(frame), end="")
print("+")
for char in list_of_char:
    print("|{:^3}".format(char), end="")
print("|")
for x in range(word_length):
    print("+{}".format(frame), end="")
print("+")
# EXERCISE 3.2
# Make a loop over integer numbers from 1 to 40.
# If x is divided by 5 then print a message ('10 is divided by 5').
# If x is divided by 7 than print a message.
# Skip x = 13.
# If x is not divided by 5 and x is not divided by 7
# then print a message ('3 is not important').
# Prepare two solutions with 'while' and 'for' loops.
print("EXERCISE 3.2:")
print("for loop:")
for x in range(1, 41):
    if x % 5 == 0:
        print(str(x) + " is divided by 5")
    if x % 7 == 0:
        print(str(x) + " is divided by 7")
    elif x == 13:
        continue
    if x % 5 != 0 and x % 7 != 0:
        print(str(x) + " is not important")
# ----------------------------------------------
print("while loop:")
n = 0
while n < 41:
    if n == 13:
        n = n + 1
        continue
    if n % 5 == 0:
        print(str(n) + " is divided by 5")
    if n % 7 == 0:
        print(str(n) + " is divided by 7")
    if n % 5 != 0 and n % 7 != 0:
        print(str(n) + " is not important")
    n = n + 1
#-----------------------------------------------
# Create the following variables:
# n = 2021
# x = math.pi   # save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"   # 'book' in English
# Write the variables to a text file "vars.txt",
# one line for one variable.
# Print the file content on the screen.
print("EXERCISE 3.3:")
import math
n = 2021
pi = math.pi
x = ("{:.5f}".format(pi))
word = "Python"
polish = "książka"
file = open("vars.txt", "w+", encoding="utf-8")
file.write("{}\n{}\n{}\n{}\n".format(n, x, word, polish))
S = file.read()
print(S)
file.close()
# I can't print the content, I don't know why...