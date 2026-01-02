from datetime import datetime

def is_birth_year_leap(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return (birth_year % 4 == 0 and birth_year % 100 != 0) or (birth_year % 400 == 0)