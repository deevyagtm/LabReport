# Represent the map as a dictionary
map_data = {
    "A": ("B", "C"),
    "B": ("A", "D"),
    "C": ("A", "D"),
    "D": ("B", "C")
}

# Ask user to enter the path
path = input("Enter the path (comma separated, e.g. A,C,D): ")

# Convert input string to list
path_list = path.split(",")

# Assume path is valid initially
valid = True

# Check each consecutive step
for i in range(len(path_list) - 1):
    current = path_list[i]
    next_node = path_list[i + 1]

    if next_node not in map_data.get(current, ()):
        valid = False
        break

# Print result
if valid:
    print("Valid path")
else:
    print("Invalid path")