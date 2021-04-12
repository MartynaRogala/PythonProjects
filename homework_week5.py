print("EXERCISE 5.1")
import os

path = os.getcwd()
print(path)
my_dir = "top"
n_pdf = 0
for root, dirs, files in os.walk(my_dir):
    for name in files:
        if name[-4:] == ".pdf":
            n_pdf += 1

print("n_pdf = {}".format(n_pdf))
print(os.path.getsize(n_pdf))

print("EXERCISE 5.2")

import datetime

date1 = datetime.date(2021, 4, 12)
date2 = datetime.date(2021, 4, 20)


def print_working_days(date1, date2):
    delta = datetime.timedelta(days=1)
    while date1 <= date2:
        if date1.isoweekday() == 1:
            print(date1)
        elif date1.isoweekday() == 2:
            print(date1)
        elif date1.isoweekday() == 3:
            print(date1)
        elif date1.isoweekday() == 4:
            print(date1)
        elif date1.isoweekday() == 5:
            print(date1)
        date1 += delta


print(print_working_days(date1, date2))
print("EXERCISE 5.3")
# Nie wiem jeszcze jak zrobić zadanie 5.3, postaram się dosłać w najbliższym czasie
