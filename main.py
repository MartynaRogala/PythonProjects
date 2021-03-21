# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# EXERCISE 2.1
# Create a long positive integer. Find the number of zeros. Hint: change the number to a string
long_positive_int = 2330404500
long_positive_int_as_string = (str(long_positive_int))
print(long_positive_int_as_string.count("0"))
# EXERCISE 2.2 (BOOL)
# Explain the results.
x = 5
x == 5 and 3  # 3
x == 4 and 3  # False - zwraca false, gdyż zmienna nie jest równa 5 ani 3
3 and x == 5  # True - zwraca true, gdyż zmienna jest równa 5
3 and x == 4  # False - zwraca false, gdyż zmienna nie jest równa 4

isinstance(True, int)  # True - zwraca true, gdyż funcja isinstance mienna nie jest 5 ani 3
isinstance(True, bool)  # True
# EXERCISE 2.3 (NUMBERS)
# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].
result = 0
# for x in result ():

# EXERCISE 3.1
# For a given word, print it in squares.
# If word = "Python", them the result is
# +---+---+---+---+---+---+
# | P | y | t | h | o | n |
# +---+---+---+---+---+---+

word = Martyna
