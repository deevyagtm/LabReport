import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset: height (in cm) and weight (in kg) for 8 people
data = {
    'Height': [150, 160, 165, 170, 175, 180, 185, 190],
    'Weight': [50, 55, 60, 65, 70, 75, 80, 85]
}

df = pd.DataFrame(data)

# Calculate mean
mean_height = np.mean(df['Height'])
mean_weight = np.mean(df['Weight'])

# Calculate variance
var_height = np.var(df['Height'], ddof=1)  # sample variance
var_weight = np.var(df['Weight'], ddof=1)

# Calculate covariance
covariance = np.cov(df['Height'], df['Weight'])[0][1]

# Calculate correlation coefficient
correlation = np.corrcoef(df['Height'], df['Weight'])[0][1]

print(f"Mean Height: {mean_height}")
print(f"Mean Weight: {mean_weight}")
print(f"Variance Height: {var_height}")
print(f"Variance Weight: {var_weight}")
print(f"Covariance: {covariance}")
print(f"Correlation Coefficient: {correlation}")

# Plot using seaborn jointplot
sns.jointplot(x='Height', y='Weight', data=df, kind='scatter')
plt.show()
