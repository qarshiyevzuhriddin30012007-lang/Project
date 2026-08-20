import json

with open("studentss.json")as file:
    studentss = json.load(file)

for talaba in studentss:

    ism = talaba["name"]
    ball = talaba["score"]

    print(f"{ism}, {ball}")

print("\nGit hub")


highest = max(studentss, key=lambda student: student["score"])

print(f"\nEng yuqori ball: {highest['name']} ({highest['score']})")