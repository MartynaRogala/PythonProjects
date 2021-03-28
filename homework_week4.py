print("EXERCISE 4.1")
import math

print("Point p = (x,y)")
x = float(input("Enter first coordinate of point in a plane (x): "))
y = float(input("Enter second coordinate of point in a plane (y): "))
r = 1
point_list = [(x, y), (x + 1, y - 1), (x * 2, y / 2), (x / 2, y)]
test_a = lambda x, y: True if math.pow(x, 2) + math.pow(y, 2) < math.pow(r, 2) else False
print("Point p is in unit circle:", test_a(x, y))
test_b = lambda x, y: True if x and y > 0 else False
print("Coordinates of p are positive: ", test_b(x, y))
point_list.sort(key=lambda p: (-p[1]))
print("List of sample p sorted by decreasing y: ", point_list)
point_list.sort(key=lambda p: (p))
print("List of sample p sorted by increasing x: ", point_list)
point_list.sort(key=lambda p: sum((abs(p[0]), abs(p[1]))))
print("List of sample p sorted by sum |x|+|y|: ", point_list)

# Pozwoliłam sobie stworzyć również narzędzie umożliwiające użytkownikowi samemu wpisać x i y.
