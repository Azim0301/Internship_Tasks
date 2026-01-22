# Each tuple contains (name, marks)
students = [
    ("Azim", 78),
    ("Dharm", 85),
    ("Bansi", 92),
    ("Avinash", 67),
    ("Aditya", 88)
]

# Find topper and average marks
total = 0
topper = students[0]

for student in students:
    total += student[1]
    if student[1] > topper[1]:
        topper = student

average = total / len(students)

print("Average Marks:", average)
print("Topper:", topper[0], "with", topper[1], "marks")
