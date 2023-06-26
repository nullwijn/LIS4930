from datetime import datetime, timedelta

def create_datetime(feet, inches):
    current_date = datetime.now().date()
    current_time = datetime.now().time()
    return datetime.combine(current_date, current_time) + timedelta(hours=feet, minutes=inches)

feet = int(input("Feet: "))
inches = int(input("Inches: "))

result = create_datetime(feet, inches)
print(result)
