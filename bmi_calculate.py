
def calculate_bmi(weight, height):
    if height <= 0:
        raise ValueError("Height must be greater than zero.")
    return weight / (height ** 2)

def bmi_category(bmi):
    
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"
