student = {
    "first_name": "Bro",
    "last_name": "Bert",
    "grade": 11
}

print(student)

for key in student.keys():
    if "name" in key:
        student[key] = None

print(student)
