print("EXERCISE 7.1")


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

    def __ne__(self, other):
        if self.x != other.x or self.y != other.y or self.z != other.z:
            return True

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
        return math.sqrt((self.x ** 2) + (self.y ** 2) + (self.z ** 2))

    def __hash__(self):
        return hash((self.x, self.y, self.z))

    def mulByInt(self, other):
        return Vector(self.x * other, self.y * other, self.z * other)


import math

v1 = Vector(1, 3, 1)
v2 = Vector(2, 2, 4)


def find_axis(v1, v2):
    v3 = Vector.cross(v1, v2)
    if v3 == Vector(0, 0, 0):
        raise ValueError("Vectors are parallel")
    v4 = v3.mulByInt(1 / v3.length())
    return v4


find_axis(v1, v2)

print("Unit vector perpendicular to the vectors v1 and v2 is: ", find_axis(v1, v2))
print("Test if v3 is unit Vector: length of v3 is: ", find_axis(v1, v2).length())
