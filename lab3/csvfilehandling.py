import csv

# Step 1: Create the CSV file with sample data
def create_csv():
    data = [
        [101, "John Doe", 85],
        [102, "Jane Smith", 90.5],
        [103, "Bob Lee", 78],
        [104, "Alice", "not_a_number"],  # invalid marks example
        [105, "Chris", 88]
    ]

    try:
        with open("students.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print("CSV file created successfully.\n")
    except Exception as e:
        print("Error creating CSV file:", e)

# Step 2: Read and display student records from CSV
def read_csv():
    try:
        with open("students.csv", "r") as file:
            reader = csv.reader(file)
            print(f"{'Roll':<6} | {'Name':<15} | {'Marks':<7}")
            print("-" * 32)
            for row in reader:
                try:
                    roll = int(row[0])
                    name = row[1]
                    marks = float(row[2])
                    print(f"{roll:<6} | {name:<15} | {marks:<7}")
                except (ValueError, IndexError):
                    print("Invalid data:", row)
    except FileNotFoundError:
        print("CSV file not found.")
    except Exception as e:
        print("An error occurred:", e)

# Main execution
create_csv()
read_csv()
