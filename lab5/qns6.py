import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Marks'].quantile(0.25)
Q3 = df['Marks'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Define lower and upper bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# Detect outliers
outliers = df[(df['Marks'] < lower_bound) | (df['Marks'] > upper_bound)]
print("\nOutliers in Marks column:")
print(outliers)

# Remove outliers
df_no_outliers = df[(df['Marks'] >= lower_bound) & (df['Marks'] <= upper_bound)]

# Verify the result
print("\nData after removing outliers:")
print(df_no_outliers)
