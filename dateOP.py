import datetime

def date1():
    current_date=datetime.datetime.now()
    hour=current_date.hour
    minute=current_date.minute
    second=current_date.second
    return print(f"The time is {hour}:{minute}:{second}.")