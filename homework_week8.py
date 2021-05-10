import numpy as np

print("Exercise 8.1")

arrayA = np.arange(0.0, 1.1, 0.1, dtype=float).reshape(11, )
print("array (a) is: \n", arrayA, "\n")
arrayB = (np.zeros([5, 6], dtype=int)).astype("int8")
print("array (b) is: \n", arrayB, "\n")
arrayC = np.arange(9, dtype=complex)
# przepraszam, ale tu nie wiem o co chodzi, gdyż nigdy nie miałam liczb zespolonych na studiach
print("array (c) is: \n", arrayC, "\n")

print("Exercise 8.2")
v1 = np.arange(0, 21, 1, dtype=int)
print("array (v1) is:", v1)
v2 = v1[1::2]
print("array (v2) is:", v2)
v3 = v1[::-1]
print("array (v3) is:", v3, "\n")

print("Exercise 8.3")

m1 = np.arange(0, 20, 1, dtype=int).reshape(4, 5)
print("array (m1) is:","\n", m1, "\n")
m2 =np.fliplr(m1)
print("array (m2) is:", "\n", m2, "\n")
m3 =np.flipud(m1)
print("array (m3) is:", "\n", m3, "\n")
m1cut = m1[1:-1,1:-1]
print("array (m1) with cutting is:", "\n", m1cut, "\n")
