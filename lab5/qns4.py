import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Check for missing values
print("Missing Values in Each Column:")
print(df.isnull().sum())

# Fill missing numerical values with column mean
df_filled = df.fillna(df.mean(numeric_only=True))

# Display DataFrame after filling missing values
print("\nData After Filling Missing Values:")
print(df_filled)
