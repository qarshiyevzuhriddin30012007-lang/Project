import json

with open("studentss.json")as file:
    studentss = json.load(file)

for talaba in studentss:

    ism = talaba["name"]
    ball = talaba["score"]

    print(f"{ism}, {ball}")

print("\nGit hub")


highest = max(studentss, key=lambda x: x["score"])
print(f"\nEng yuqori ball: {highest["name"]} ({highest["score"]})")

lowest = min(studentss, key=lambda x: x["score"])
print(f"\nEng past ball: {lowest["name"]} ({lowest["score"]})")
