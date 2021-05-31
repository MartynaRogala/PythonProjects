import math
import numpy as np
import matplotlib.pyplot as plt

# Exercise1
D, Nx, Nt = 2, 20, 150
x = np.linspace(0, -1.0, Nx + 1)
dx = 1.0 / Nx
dt = 0.01 / Nt
r = D * dt / (dx * dx)
assert r < 1
u = np.empty((Nx + 1, Nt + 1), dtype=float)
u[:, 0] = -5.5 * x * (1 - x)
u[0, :] = -1.0
u[Nx, :] = 3.0
for j in range(Nt):
    u[1:-1, j + 1] = r * u[:-2, j] + (1 - 2 * r) * u[1:-1, j] + r * u[2:, j]
print(u)
plt.title("1D heat equation")
plt.xlabel("time")
plt.ylabel("x")
plt.imshow(u, cmap="hot", interpolation="nearest")
plt.show()
# Exercise 11.2
Nx, Nt, L, T = 400, 1000, 1, 2
t = np.linspace(0, T, num=Nt + 1, dtype=float)
x = np.linspace(0, L, num=Nx + 1, dtype=float)
c = 1.0
dx = x[1] - x[0]
dt = t[1] - t[0]
r = (c * dt / dx) ** 2
assert r < 2
u = np.empty((Nx + 1, Nt + 1), dtype=float)
u[:, 0] = np.where(x < 0.5, 2 * x, 2 * (1 - x))
assert u[0, 0] == 0 and u[Nx, 0] == 0
u[0, :] = 1
u[Nx:] = -1
for k in range(1, Nt):
    u[1:-1, k + 1] = -u[1:-1, k - 1] + 2 * u[1:-1, k] + r * (u[:-2, k] - 2 * u[1:-1, k] + u[2:, k])
plt.title("1D wave equation")
plt.xlabel("t")
plt.ylabel("x")
plt.imshow(u, cmap="hot", interpolation="nearest")
plt.show()
