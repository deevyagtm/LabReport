from functools import reduce

students = ["Amit", "Sita", "Ramesh", "Anita"]
scores = [78, 85, 90, 88]

# Pair names and scores
student_scores = list(zip(students, scores))
print("Student Scores:", student_scores)

# Calculate total score
total_score = reduce(lambda x, y: x + y, scores)

print("Total Score:", total_score)
