def write_file():
    try:
        with open("menu.txt", "w") as f:
            data = input("Enter data to write: ")
            f.write(data + "\n")
            print("Data written successfully")
    except Exception as e:
        print("Error:", e)

def read_file():
    try:
        with open("menu.txt", "r") as f:
            print("\nFile Contents:")
            print(f.read())
    except FileNotFoundError:
        print("File not found")

def append_file():
    try:
        with open("menu.txt", "a") as f:
            data = input("Enter data to append: ")
            f.write(data + "\n")
            print("Data appended successfully")
    except Exception as e:
        print("Error:", e)

while True:
    print("\n1. Write\n2. Read\n3. Append\n4. Exit")
    try:
        choice = int(input("Enter choice: "))
        if choice == 1:
            write_file()
        elif choice == 2:
            read_file()
        elif choice == 3:
            append_file()
        elif choice == 4:
            print("Exiting program")
            break
        else:
            print("Invalid choice")
    except ValueError:
        print("Please enter a valid number")
