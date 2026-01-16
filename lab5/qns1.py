import pandas as pd

# Create a dictionary with sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 21, 19, 20],
    "Marks": [58, 72, 65, 90, 45]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data)

# Display first 5 rows
print("First 5 Rows:")
print(df.head())

# Display dataset shape
print("Shape (Rows, Columns):", df.shape)

# Save DataFrame to CSV file
# we kept index as false to avoid writing row numbers to the file which means we don't want to save the index
df.to_csv("sample_data.csv", index=False)

