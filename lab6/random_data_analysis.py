import numpy as np
import matplotlib.pyplot as plt

# Generate two random datasets with no clear relationship
np.random.seed(0)  # For reproducibility
data1 = np.random.rand(50) * 100
data2 = np.random.rand(50) * 100

# Compute covariance
covariance = np.cov(data1, data2)[0][1]
print("Covariance:", covariance)

# Compute correlation
correlation = np.corrcoef(data1, data2)[0][1]
print("Correlation:", correlation)

# Scatter plot
plt.scatter(data1, data2)
plt.xlabel("Dataset 1")
plt.ylabel("Dataset 2")
plt.title("Scatter Plot of Two Random Datasets")
plt.show()
