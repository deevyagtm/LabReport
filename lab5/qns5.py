import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Detect duplicate rows
duplicates = df.duplicated()
print("Duplicate Rows (True means duplicate):")
print(duplicates)

# Count total duplicates
print("\nNumber of duplicate rows:", duplicates.sum())

# Remove duplicate rows
df_no_duplicates = df.drop_duplicates()

# Verify result
print("\nData after removing duplicates:")
print(df_no_duplicates)

print("\nShape before removing duplicates:", df.shape)
print("Shape after removing duplicates:", df_no_duplicates.shape)
