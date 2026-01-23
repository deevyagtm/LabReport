import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Dataset
hours_studied = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
marks_scored = np.array([35, 40, 45, 55, 60, 65, 70, 80, 85, 90])

# Correlation coefficient
correlation = np.corrcoef(hours_studied, marks_scored)[0][1]
print("Correlation Coefficient:", correlation)

# Regression plot
sns.regplot(x=hours_studied, y=marks_scored)
plt.xlabel("Hours Studied")
plt.ylabel("Marks Scored")
plt.title("Regression Plot of Hours Studied vs Marks Scored")
plt.show()
