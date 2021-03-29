#Treść zadania:
#Reversing a part of a list in place, reverse_range(L, left, right), the right index is included. Write iterative and recursive versions.

#Wg mnie chodzi o to że on chce pętle która będzie zwracać liste w której tylko kawałek będzie odwócony: np:
# L1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# L2 = [0, 1, 5, 4, 3, 2, 6, 7, 8, 9]

#i że ma być to zrobione w sposówb (1) iterative i (2) recursive

# tu jest różnica pomiędzy (1) iterative i (2) recursive https://stackoverflow.com/questions/51994148/recursive-vs-iterative-functions-python
# a tu kod. moim zadniem ten kod poniżej jest w sposób iterative i teraz potrzeba w ten drugi sposób
def reverse(seq, start, stop):
    size = stop + start
    for i in range(start, stop):
        j = size - i
        seq[i], seq[j] = seq[j], seq[i] #nie rozumiem co tu sie dzieje ale jesli to jest to co obracaca to uzyj w rekruencji

l = list(range(10))
print(l)
reverse(l, 2, 5)
print(l)

## powinnas jesli chcesz rekurencje to powinnaś zrobic cos w stylu 

def recusive_reverse(seq, start, stop):
    if(len(size) == 1) #jesli duglosc listy jest 1 
        return seq[0]
    else
    # obroć liste coś takiego 
    
# nie mam pyharma wiec ciezko mi to jednak ogarnac jak wroce do domu to przekminimy
