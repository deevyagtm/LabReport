import pandas as pd

# Load the CSV file
df = pd.read_csv("sample_data.csv")

# Select rows where Marks > 60
filtered_df = df[df["Marks"] > 60]

# Select only Name and Marks columns
result = filtered_df[["Name", "Marks"]]

# Display the result
print(result)
