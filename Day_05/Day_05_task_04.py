students = [
    {"name": "Azim", "marks": 78},
    {"name": "Dharm", "marks": 35},
    {"name": "Bansi", "marks": 88},
    {"name": "Avinash", "marks": 42}
]

passed_students = [
    s["name"] for s in students if s["marks"] >= 40
]

failed_students = [
    s["name"] for s in students if s["marks"] < 40
]

print("Passed Students:", passed_students)
print("Failed Students:", failed_students)
