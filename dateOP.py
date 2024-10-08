import datetime 

def currentDate ():
    '''
    This function retrieves the current date using the `datetime.date.today()` 
    method and prints it in a formatted string.

    '''
    day = datetime.date.today()
    print(f"This si currently date:{day}")

