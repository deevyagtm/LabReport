import numpy as np
import matplotlib.pyplot as plt

# Dataset for 10 students
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks_scored = np.array([35, 40, 45, 55, 60, 65, 70, 80, 85, 90])

# Calculate covariance
covariance = np.cov(hours_studied, marks_scored)[0][1]
print("Covariance between hours studied and marks scored:", covariance)

# Scatter plot
plt.scatter(hours_studied, marks_scored)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Scatter Plot of Hours Studied vs Marks Scored")
plt.show()
