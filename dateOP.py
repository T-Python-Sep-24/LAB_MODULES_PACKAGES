import datetime

def date1():
    current_date=datetime.datetime.today()
    year=current_date.year
    month=current_date.month
    day=current_date.day
    return print(f"The date is {year}-{month}-{day}")