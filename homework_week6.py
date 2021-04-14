class Vector:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return "Vector({}, {}, {})".format(self.x, self.y, self.z)

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y or self.z != other.z:
            return True
        else:
            return False

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def cross(self, other):
        return Vector((self.y * other.z) - (self.z * other.y),
                      (self.z * other.x) - (self.x * other.z),
                      (self.x * other.y) - (self.y * other.x))

    def length(self):
        return math.sqrt((self.x ** 2) + (self.y ** 2))

    def __hash__(self):
        return hash((self.x, self.y, self.z))


# Exemplary tests:
import math

v = Vector(1, 1, 1)
w = Vector(2, 2, 2)
assert (repr(v)) == "Vector(1, 1, 1)"
assert (repr(w)) == "Vector(2, 2, 2)"
assert v != w
assert v + w == Vector(3, 3, 3)
assert v - w == Vector(-1, -1, -1)
assert v * w == 6
assert Vector.cross(v, w) == Vector(0, 0, 0)
assert Vector.length(v) == math.sqrt(2)
assert w.length() == math.sqrt(8)

print("Tests passed")

# My notes for tests:
# import math
# v = Vector(1, 1, 1)
# w = Vector(2, 2, 2)
# print(repr(v))
# print(repr(w))
# print(Vector.__eq__(v, w))
# print(Vector.__ne__(v, w))
# print(Vector.__add__(v, w))
# print(Vector.__sub__(v, w))
# print(Vector.__mul__(v, w))
# print(Vector.cross(v, w))
# print(Vector.length(v))
# print(Vector.length(w))
# print(Vector.__hash__(v))
# print(Vector.__hash__(w))
