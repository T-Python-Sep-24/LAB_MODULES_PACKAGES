#Import date class only from datetime module 
from datetime import date

#Defining a function to print the date
def currentDate():
    '''
    This function prints today's date when called 
    '''
    today = date.today()
    print(f"Today's date is: {today}")
    