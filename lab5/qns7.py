import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Create a new column by transforming Marks (Marks divided by 10)
df['Marks_Scaled'] = df['Marks'] / 10

# Rename columns (for example: Name -> Student_Name, Marks -> Total_Marks)
df.rename(columns={'Name': 'Student_Name', 'Marks': 'Total_Marks'}, inplace=True)

# Display the cleaned DataFrame
print("Cleaned DataFrame:")
print(df)

# Save the cleaned dataset to a new CSV file
df.to_csv("cleaned_data.csv", index=False)
print("\nCleaned dataset saved as 'cleaned_data.csv'")
