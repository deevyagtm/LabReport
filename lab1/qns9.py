celsius = float(input("Enter temperature in Celsius: "))
print("1. Fahrenheit")
print("2. Kelvin")

choice = int(input("Enter your choice: "))

if choice == 1:
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)
else:
    print("Invalid choice")
