import numpy as np
import matplotlib.pyplot as plt

# Dataset: Daily temperature (°C) and ice-cream sales
temperature = np.array([20, 22, 24, 26, 28, 30, 32, 34, 36, 38])
ice_cream_sales = np.array([120, 135, 150, 170, 190, 210, 235, 260, 290, 320])

# Calculate covariance
covariance = np.cov(temperature, ice_cream_sales)[0][1]
print("Covariance between temperature and ice-cream sales:", covariance)

# Scatter plot
plt.scatter(temperature, ice_cream_sales)
plt.xlabel("Daily Temperature (°C)")
plt.ylabel("Ice-cream Sales")
plt.title("Scatter Plot of Temperature vs Ice-cream Sales")
plt.show()
