students = {}

n = input("Enter number of students: ")

if not n.isdigit():
    print("Please enter correct input value")
else:
    n = int(n)

    for i in range(n):
        name = input("Enter student name: ")
        marks_input = input("Enter marks separated by space: ")

        if name == "":
            print("Please enter correct input value")
            break

        marks_list = marks_input.split()
        marks = []
        valid = True

        for m in marks_list:
            if m.isdigit():
                marks.append(int(m))
            else:
                valid = False

        if valid == False or len(marks) == 0:
            print("Please enter correct input value")
            break

        students[name] = marks

    avg_list = []

    for name in students:
        total = 0
        for m in students[name]:
            total = total + m

        avg = total / len(students[name])

        if avg >= 80:
            grade = "A"
        elif avg >= 60:
            grade = "B"
        elif avg >= 40:
            grade = "C"
        else:
            grade = "D"

        print(name, "Average:", avg, "Grade:", grade)

        avg_list.append([name, avg])

    top = 2  # fixed top students

    if top > len(avg_list):
        print("Please enter correct input value")
    else:
        # simple sorting based on average (descending)
        for i in range(len(avg_list)):
            for j in range(i + 1, len(avg_list)):
                if avg_list[j][1] > avg_list[i][1]:
                    temp = avg_list[i]
                    avg_list[i] = avg_list[j]
                    avg_list[j] = temp

        print("Top 2 students:")
        for i in range(top):
            print(avg_list[i][0], "with average", avg_list[i][1])
