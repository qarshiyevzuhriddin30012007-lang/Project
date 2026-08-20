import json

with open("students.json")as file:
    students = json.load(file)

print(students)