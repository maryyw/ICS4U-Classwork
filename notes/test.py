from typing import Dict

assignment_list = []

while True:
    name = None
    due = None
    points = None
    name = input("Enter assignment name: ")
    due = input("Enter assignment due date: ")
    points = input("Enter number of points: ")
    new_assignment = {
        "name": name, "due_date": due,
        "points": points
    }
    assignment_list.append(dict(new_assignment))
    if input("""
        Press space then enter to view assignments or
        Press enter to add more assignments:
            """) == " ":
        break

return assignment_list
