# Create sample file
with open("numbers.txt", "w") as f:
    f.write("10\n20\nabc\n30.5\n")

total = 0
count = 0

with open("numbers.txt") as f:
    for line in f:
        try:
            num = float(line)
        except:
            continue
        total += num
        count += 1


if count > 0:
    print("Sum =", total)
    print("Average =", total / count)
else:
    print("No valid numbers found")
