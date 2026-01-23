import numpy as np
import matplotlib.pyplot as plt

# Generate X values
np.random.seed(42)
X = np.arange(1, 21)  # 1 to 20

# Y increases linearly with X (plus a little noise)
Y = 3 * X + 5 + np.random.normal(0, 2, size=X.size)

# Z increases randomly (no clear relationship with X)
Z = np.random.rand(X.size) * 60

# Compute covariance and correlation for (X, Y)
cov_XY = np.cov(X, Y)[0][1]
corr_XY = np.corrcoef(X, Y)[0][1]

# Compute covariance and correlation for (X, Z)
cov_XZ = np.cov(X, Z)[0][1]
corr_XZ = np.corrcoef(X, Z)[0][1]

print(f"Linear case - Covariance: {cov_XY:.2f}, Correlation: {corr_XY:.2f}")
print(f"Random case - Covariance: {cov_XZ:.2f}, Correlation: {corr_XZ:.2f}")

# Plotting
fig, axs = plt.subplots(1, 2, figsize=(12, 5))

# Linear relationship plot
axs[0].scatter(X, Y, color='blue')
axs[0].set_title('Linear Relationship (X vs Y)')
axs[0].set_xlabel('X')
axs[0].set_ylabel('Y')

# Random relationship plot
axs[1].scatter(X, Z, color='red')
axs[1].set_title('Random Relationship (X vs Z)')
axs[1].set_xlabel('X')
axs[1].set_ylabel('Z')

plt.tight_layout()
plt.show()
