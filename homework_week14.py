import numpy as np
print("Exercise 14.1")
points_number = (int(input("Enter number of points for pi estimation in range: 10 - 10^6: ")))
x = np.random.rand(points_number)
y = np.random.rand(points_number)
d = np.sqrt(pow(x,2)+pow(y,2))
circle_points = np.where(d<=1)
circle_points1= d[circle_points]
ratio_for= 4 * (len(circle_points1) / points_number)
print("Estimated pi value for", points_number, "points (using Monte Carlo method) is:", ratio_for)
