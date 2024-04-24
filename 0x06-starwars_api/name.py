students = []

with open(students.csv) as file:
    for line in file:
        name, home = line.rstrip().split(",")
        student = {}
        student["name"] = name
        student["home"] = home
        student.append(student)

    for student in students:
        print(f"{name} is in {home}")