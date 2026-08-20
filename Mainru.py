import json

with open("studentss.json")as file:
    studentss = json.load(file)

for talaba in studentss:

    ism = talaba["name"]
    ball = talaba["score"]

    print(f"{ism}, {ball}")

print("Git hub")
