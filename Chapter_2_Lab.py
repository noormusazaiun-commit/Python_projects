scores = [85, 72, 45, 90, 60, 55, 78, 92, 60, 40, 88, 72]

print("Scores:", scores)


minimum = min(scores)
maximum = max(scores)
average = sum(scores) / len(scores)

print("Minimum:", minimum)
print("Maximum:", maximum)
print("Average:", average)


passed_scores = [score for score in scores if score >= 60]

print("Passed scores:", passed_scores)


score_set = set(scores)

print("Set of scores:", score_set)


students = {
    101: "Ahmad",
    102: "Hamid",
    103: "Ali",
    104: "Basit",
    105: "Omid"
}

print("Students:", students)



student_id = 103

if student_id in students:
    print("Student:", students[student_id])
else:
    print("Student not found")

records = [
    ("Ahmad", 85),
    ("Hamid", 72),
    ("Ali", 45),
    ("Basit", 90),
    ("Omid", 60)
]

sorted_records = sorted(records, key=lambda student: student[1])

print("Sorted by score:")
for student in sorted_records:
    print(student)


print("\nStudents with numbers:")

for number, student in enumerate(records, start=1):
    print(number, student)


names = ["Ahmad", "Hamid", "Ali", "Basit", "Omid"]
student_scores = [85, 72, 45, 90, 60]

print("\nNames and scores:")

for name, score in zip(names, student_scores):
    print(name, ":", score)

    