import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv("sample_data.csv")

# Display column names
print("Column Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Display basic statistics
print("\nBasic Statistics:")
print(df.describe()) # Describe gives count, mean, std, min, 25%, 50%, 75%, max for numerical columns
