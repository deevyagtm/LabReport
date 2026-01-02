import random


students = ["Alice", "Bob", "Alice", "Diana", "Bob", "Fiona"]


unique_students = list(set(students))


if len(unique_students) < 3:
    print("Not enough unique students to select 3 volunteers.")
else:
    volunteers = random.sample(unique_students, 3)
    print("Selected volunteers for the presentation:")
    for volunteer in volunteers:
        print(volunteer)

