from datetime import datetime, time
import random

def temperature():
    # Get the current time
    current_time = datetime.now().time()

    # Define the start and end times
    start_time = time(21, 0)  # 21:00
    end_time = time(9, 0)  # 9:00

    # Check if the current time is between the start and end times
    if start_time <= current_time or current_time <= end_time:
        random_number = random.randint(-5, 5)
        return random_number
    else:
        random_number = random.randint(5, 15)
        return random_number
    
def humidity():
    current_month = datetime.now().month
    
    # Check if the current time is between the january and june
    if current_month == 1 or current_month == 6:
        random_number = random.randint(10, 20)
        return random_number
    else:
        random_number = random.randint(15, 25)
        return random_number

    