# Write multiple lines to a file
try:
    file = open("sample.txt", "w")
    file.write("Hello World\n")
    file.write("This is Lab 3\n")
    file.write("File Handling in Python\n")
    file.close()
    print("Data written successfully")
except Exception as e:
    print("Error while writing:", e)

# Read the file
try:
    file = open("sample.txt", "r")
    print("\nFile Contents:")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("File does not exist")
