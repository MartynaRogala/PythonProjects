import numpy as np
import matplotlib.pyplot as plt

#Exercise 9.1
x = np.linspace(0,10,1000)
y1 = np.sin(x)
plt.plot(x, y1, c ="red", linestyle="solid", label="sin(x)")
y2 = np.cos(x)
plt.plot(x, y2, c ="green", linestyle="dashed", label="cos(x)")
x = np.linspace(0,10,1000)
y3 = np.exp(-x)
plt.plot(x, y3, c ="blue", linestyle="dotted", label="exp(-x)")
plt.title("Exercise 9.1")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()
# Exercise 9.2
points_number = 100
x = np.random.rand(points_number)
y = np.random.rand(points_number)
colors = ['g' if dot else 'r' for dot in x ** 2 + y ** 2 < 1]
size_of_dot = (x+y)*(points_number/4)
plt.scatter(x, y, c=colors, s=size_of_dot)
plt.title("Exercise 9.2")
plt.xlabel("x")
plt.ylabel("y")
plt.show()
