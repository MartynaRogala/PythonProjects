import pandas as pd

print("Exercise 10.2\nWind force forecast for the next few days:\n")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
wind_force = [6, 21, 16, 14, 18, 16, 14]
forecast = pd.Series(data=wind_force, index=days)
print(forecast)

print("\nExercise 10.3\nTen elements from periodic table:\n")

index = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
name = ["Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon"]
symbol = ["H", "He", "Li", "Be", "B", "C", "N", "O", "F", "N", ]
weight = [1, 4, 7, 9, 11, 12, 14, 16, 19, 20]
dict = {"Name": name, "Symbol": symbol, "Weight": weight}
periodic = pd.DataFrame(data=dict, index=index, dtype=object)
print(periodic)
