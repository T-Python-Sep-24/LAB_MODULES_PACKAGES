# for now()
from datetime import datetime
# for timezone()
import pytz


current_time:str
def func_date():
    current_time:str
    current_time = datetime.now(pytz.timezone('Asia/Riyadh'))
    print("The current time in Riyadh is :", current_time)
    
    # Get the current date and time
    date_now = datetime.now()
    print(f"Current date is: {date_now.strftime('%d/%m/%Y')}")
    
    print("The current time in Riyadh is:", current_time.strftime('%d/%m/%Y %H:%M:%S'))
    
    
    return current_time


func_date()