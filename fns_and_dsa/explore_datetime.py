import datetime

def display_current_datetime():
    current_date= datetime.datetime.now()
    print(f'Current date and time {current_date.strftime("%Y-%m-%d %H:%M:%s")}')
    return 

display_current_datetime()
#future date
from datetime import timedelta
number_of_days= int(input('Enter the number of days to add to the current date: '))
def calculate_future_date():
    today = datetime.datetime.now()
    future_date = today + timedelta(days=number_of_days)
    print(f'Future_date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}')

calculate_future_date()