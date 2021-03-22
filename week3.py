# EXERCISE 3.1
# For a given word, print it in squares.
# If word = "Python", them the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
# word = "Martyna"
# list_of_char = tuple(word)
# frame = "+-"
# frame_list=tuple(frame)
# print(frame_list)
# for symbol in frame_list:
#     print("+".format(symbol), end='')
# for char in list_of_char:
#     print("{0[0]}".format(char), end="")
#     print("{:^3}|".format(char), end="")
# coord = (3, 5)
# "x {0[0]}  y {0[1]}".format(coord)   # 'x 3 y 5'

# Make a loop over integer numbers from 1 to 40.
# If x is divided by 5 then print a message ('10 is divided by 5').
# If x is divided by 7 than print a message.
# Skip x = 13.
# If x is not divided by 5 and x is not divided by 7
# then print a message ('3 is not important').
# Prepare two solutions with 'while' and 'for' loops.

# list_of_numbers= range(start_1,stop_41)
# print(list_of_numbers)
# print(a % b)
# print(a / b)
# print(a // b)
# for x in range(1, 41):
#     if x % 5 == 0:
#         print(str(x) + " is divided by 5")
#     if x % 7 == 0:
#         print(str(x) + " is divided by 7")
#     elif x == 13:
#         continue
#     if x % 5 != 0 and x % 7 != 0:
#         print(str(x) + " is not important")
#----------------------------------------------
n=1
while n in range(1,41):
    if n % 5 == 0:
        print(str(n) + " is divided by 5")
    n = n + 1
    if n % 7 == 0:
        print(str(n) + " is divided by 7")
    elif n == 13:
        continue
    if n % 5 != 0 and n % 7 != 0:
        print(str(n) + " is not important")
#-----------------------------------------------
# Create the following variables:
# n = 2021
# x = math.pi   # save with 5 digits after a dot (import 'math' first!)
# word = "Python"
# polish = "książka"   # 'book' in English
# Write the variables to a text file "vars.txt",
# one line for one variable.
# Print the file content on the screen.
