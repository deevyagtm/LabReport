import pandas as pd
import random

# --------------------
# 1. Generate fake student info
# --------------------
student_count = 5  # number of students

students = pd.DataFrame({
    "rollno": range(1, student_count+1),
    "name": [f"Student{i}" for i in range(1, student_count+1)],
    "mother_name": [f"Mother{i}" for i in range(1, student_count+1)],
    "father_name": [f"Father{i}" for i in range(1, student_count+1)],
    "nationality": ["Nepalese"]*student_count,
    "gender": [random.choice(["M","F"]) for _ in range(student_count)]
})

# --------------------
# 2. Generate fake marks table
# --------------------
terms = ["Term1", "Term2", "Term3", "Term4"]
subjects = ["Math", "English", "Science", "Nepali"]

marks_data = []

for roll in students["rollno"]:
    for term in terms:
        for subject in subjects:
            marks_data.append({
                "rollno": roll,
                "term": term,
                "subject": subject,
                "marks": random.randint(50, 100)  # random marks 50-100
            })

marks = pd.DataFrame(marks_data)

# --------------------
# 3. First table: marks
# --------------------
print("---- Marks Table ----")
print(marks.head(16))  # show first few rows

# --------------------
# 4. Second table: student info + average
# --------------------
avg_marks = marks.groupby("rollno")["marks"].mean().reset_index()
avg_marks.rename(columns={"marks":"Average_Marks"}, inplace=True)

final_table = pd.merge(students, avg_marks, on="rollno")

print("\n---- Student Info with Average Marks ----")
print(final_table)
