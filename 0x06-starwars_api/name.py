import csv

name = input("what;s your name? ")
home = input("where do you live? ")

with open("students.csv") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})