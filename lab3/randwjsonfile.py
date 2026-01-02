import json

student = {
    "id": 1,
    "name": "Divya",
    "marks": 85
}

# Write JSON
try:
    with open("student.json", "w") as file:
        json.dump(student, file)
        print("JSON data written successfully")
except Exception as e:
    print("Write error:", e)

# Read JSON
try:
    with open("student.json", "r") as file:
        data = json.load(file)
        print("\nStudent Details:")
        print("ID:", data["id"])
        print("Name:", data["name"])
        print("Marks:", data["marks"])
except FileNotFoundError:
    print("JSON file not found")
except json.JSONDecodeError:
    print("Invalid JSON format")
