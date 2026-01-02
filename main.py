import leap_year
import bmi_calculate
import army_eligibility

# This is input from user
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meters: "))

# Leap Year
if leap_year.is_birth_year_leap(age):
    print("Your birth year was a leap year.")
else:
    print("Your birth year was not a leap year.")
# BMI
user_bmi = bmi_calculate.calculate_bmi(weight, height)
category = bmi_calculate.bmi_category(user_bmi)
print(f"Your BMI is: {user_bmi:.2f}, Category: {category}")

# Army
if army_eligibility.is_eligible(age, user_bmi):
    print("You are eligible for army entrance.")
else:
    print("You are NOT eligible for army entrance.")
