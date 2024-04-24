students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split()
        student = {}
        student["name"] = name
        student["house"] = house