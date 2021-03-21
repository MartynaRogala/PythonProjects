# EXERCISE 3.1
# For a given word, print it in squares.
# If word = "Python", them the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+
word = "Martyna"
list_of_char = tuple(word)

for char in list_of_char:
    print("{0[0]}".format(char), end="")
    print("{:^3}|".format(char), end="")
coord = (3, 5)
"x {0[0]}  y {0[1]}".format(coord)   # 'x 3 y 5'