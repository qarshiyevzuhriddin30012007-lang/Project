import json

def analyze_students():

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

    ball = [student["score"] for student in studentss]
    ortacha = sum(ball) / len(ball)

    print(f"\nTalabalarning o'rtacha bali: {ortacha:.1f}")

    filtered_students = [
        student["name"]
        for student in studentss
        if student["score"] > 80
    ]

    print("\n80 dan yuqori olganlar:")
    print(filtered_students)

analyze_students()