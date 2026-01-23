import numpy as np

# Dataset
temperature = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38])
ice_cream_sales = np.array([120, 135, 150, 170, 190, 210, 235, 260, 290, 320])

# Calculate covariance
covariance = np.cov(temperature, ice_cream_sales)[0][1]
print("Covariance:", covariance)

# Calculate correlation coefficient
correlation = np.corrcoef(temperature, ice_cream_sales)[0][1]
print("Correlation Coefficient:", correlation)

# Explanation
print("\nExplanation:")
print("Covariance shows how two variables change together but depends on units, so its magnitude is hard to interpret.")
print("Correlation is standardized between -1 and +1, showing both direction and strength clearly.")
