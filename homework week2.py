print("EXERCISE 2.1", "\n")
# Create a long positive integer. Find the number of zeros. Hint: change the number to a string.
long_positive_int = 12340055670
long_positive_int_as_string = str(long_positive_int)
print("Number of zeros in number", str(long_positive_int), "is: ", long_positive_int_as_string.count("0"))
print("")

print("EXERCISE 2.2 (BOOL)", "\n")
x = 5
print(x == 5 and 3, "because 'True and Anything' returns 'Anything', but not converted to 'bool'")
print(x == 4 and 3, "because x = 5, and it is not 4 and 3 ")
print(3 and x == 5, "because x = 5")
print(3 and x == 4, "because x = 5, and it is not 4 and 3 ")
print(isinstance(True, int), "because 'True' can be treated as int")
print(isinstance(True, bool), "because 'True' can be treated as bool")
print("")

print("EXERCISE 2.3 (NUMBERS)", "\n")
# Find the sum 1*1 + 3*3 + 5*5 + ... + 2021*2021 [hint: use sum()].
start = 1
stop = 2022
step = 2
result = 0
for x in range(start, stop, step):
    result += x * x
print("Sum of given equation is: ", result)
print("")

print("EXERCISE 2.4 (STR)", "\n")
polish_alphabet = ["ą", "ć", "ę", "ł", "ń", "ó", "ś", "ź", "ż"]
print("(a) Unicode points for polish characters are: ")
for pl in polish_alphabet:
    print(ascii(pl))
polish_alphabet_encoded = []
chars_with_one_byte = []
chars_with_two_byte = []
chars_with_three_byte = []
chars_with_four_byte = []

for char in polish_alphabet:
    polish_alphabet_encoded.append(char.encode())

for encoded_char in polish_alphabet_encoded:
    amount_of_bytes = len(encoded_char)
    decoded_char = ascii(encoded_char)

    if amount_of_bytes == 1:
        chars_with_one_byte.append(decoded_char)
    elif amount_of_bytes == 2:
        chars_with_two_byte.append(decoded_char)
    elif amount_of_bytes == 3:
        chars_with_three_byte.append(decoded_char)
    elif amount_of_bytes == 4:
        chars_with_four_byte.append(decoded_char)

print("(c) List of unicode characters presented in binary representation with:")
print("1 byte:", (chars_with_one_byte))
print("2 bytes:", (chars_with_two_byte))
print("3 bytes:", (chars_with_three_byte))
print("4 bytes:", (chars_with_four_byte))

print("(c) Periodic table:")
pt = [(1, "Hydrogen", "H", 1), (2, "Helium", "He", 4), (3, "Lithium", "Li", 7), (4, "Beryllium", "Be", 9),
      (5, "Boron", "B", 11), (6, "Carbon", "C", 12), (7, "Nitrogen", "N", 14), (8, "Oxygen", "O", 16),
      (9, "Fluorine", "F", 19), (10, "Neon", "Ne", 20)]
titles = ("No.", "Name (en)", "Symbol", "Weight (u)")
frame = ("+{:->3}+{:-<20}+{:-^6}+{:->10}+".format("", "", "", ""))
print(frame)
print("|{0:>3}|{1:<20}|{2:^6}|{3:>10}|".format(titles[0], titles[1], titles[2], titles[3]))
print(frame)
pt_size = len(pt)
for char in range(pt_size):
    print("|{0:>3}|{1:<20}|{2:^6}|{3:>10}|".format(pt[char][0], pt[char][1], pt[char][2], pt[char][3]))
print(frame)
print("")

print("EXERCISE 2.5 (LIST)", "\n")
S = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s."
words_in_S = S.split()
number_of_words = len(words_in_S)
print("The number of words in S is: ", number_of_words)
black_char = 0
for char in S:
    if char != ' ':
        black_char += 1
print("The number of black characters in S is: ", black_char)


def find_longest_word(word_list):
    longest_word = max(word_list, key=len)
    return longest_word


print("The longest word in S is: ", find_longest_word(words_in_S))
print("(1) Words in lexicographic order: ", sorted(words_in_S))
print("(2) Words in length order: ", sorted(words_in_S, key=len))
print("")

print("EXERCISE 2.6 (TUPLE)", "\n")
print("Code from exercise can't work because: \n t = (2, 4) \n print(t[2]) \n t.append(6)")
print(
    "Explanation 1: print(t[2]) returns: \"IndexError: tuple index out of range\", because t has only two obcjets, t[2] could be a third object.")
print(
    "Explanation 2: t.append(6) returns: \"AttributeError: 'tuple' object has no attribute 'append'\", because t is a tuple not a list")
print(
    "To obtain t[2] we should write for example this: \n t = (2, 4) \n t_as_list = list(t) \n t_as_list.append(6) \n print(t_as_list[2])")
# Niestety nie rozumiem tego stwierdzenia: a, b = t ; print(a, b). Czy może Pan wytłumaczyć o co chodziło?
print("")

print("EXERCISE 2.7 (DICT)", "\n")
roman_numerals = ["I", "V", "X", "L", "C", "D", "M"]
arabic_numbers = ["1", "5", "10", "50", "100", "500", "1000"]
D1 = {}
D1["I"] = "1";
D1["V"] = "5";
D1["X"] = "10";
D1["L"] = "50";
D1["C"] = "100";
D1["D"] = "500";
D1["M"] = "1000"
D2 = {"I": "1", "V": "5", "X": "10", "L": "50", "C": "100", "D": "500", "M": "1000"}
D3 = dict([("I", "1"), ("V", "5"), ("X", "10"), ("L", "50"), ("C", "100"), ("D", "500"), ("M", "1000")])
D4 = dict(zip(["I", "V", "X", "L", "C", "D", "M"], ["1", "5", "10", "50", "100", "500", "1000"]))
print("Dictionary created by method 1: ", D1)
print("Dictionary created by method 2: ", D2)
print("Dictionary created by method 3: ", D3)
print("Dictionary created by method 4: ", D4)
