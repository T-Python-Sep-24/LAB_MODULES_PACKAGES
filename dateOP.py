#function that when called prints the current date.
from datetime import datetime

def print_current_date():
    current_date = datetime.now().date()
    print("Current date:", current_date)


if __name__ == "__main__":
    print_current_date()

