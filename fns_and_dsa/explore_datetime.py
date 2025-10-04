

import datetime
from datetime import timedelta





def display_current_datetime():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {current_date}")


display_current_datetime()


def calculate_future_date():
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    Added_time = int(
        input("Enter the number of days to add to the current date: "))
    future_date = current_time + timedelta(days=Added_time)
    print(f"Future date: {future_date}")


calculate_future_date()
