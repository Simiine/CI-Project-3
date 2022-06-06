import datetime
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('events_planner')
EVENTS = SHEET.worksheet('events')

def menu():
    """
    Display menu with list of options to choose from
    """
    while True:
        print("Welcome to your Digital Planner.\n")
        print("""
                    ------Menu------
                    1. Add Event
                    2. Display All Events
                    3. Search Event
                    4. Delete Event
                    5. Reset
                    6. Exit
                    """)

        option = input("Choose options from 1 - 6: ")
        if option == "1":
            add_event()
        elif option == "2":
            display_all_events()
        elif option == "3":
            search_event()
        elif option == "4":
            delete_event()
        elif option == "5":
            reset()
        elif option == "6":
            exit()
        else:
            print("Invalid option, please select number from 1 - 6: ")

def add_event():
    """
    Adds new event to the excel file with the following information
    Title, date, start time, end time, location, Description
    """
    event_details = []
    while True:
        title = input("Enter the event title: ")
        if validate_data(title):
            event_details.append(title)
            break
    while True:
        date = input("Enter date: ")
        if validate_date(date):
            event_details.append(date)
            break
    
def validate_data(values):
    """
    Validate to check if string inputs contain only letters
    """
    try: 
        if values.isalpha() is False:
            raise ValueError()
    except ValueError as e:
        print("Data is invalid, please ensure you are only using letters.\n")
        return False
    return True

def validate_date(date):
    """
    Validate date to check it is in the right format dd/mm/yy
    """
    try:
        if datetime.datetime.strptime(date, '%d-%m-%Y') is False:
            raise ValueError()
    except ValueError as e:
        print("Incorrect data format, should be DD-MM-YYYY.\n")
        return False
    return True


menu()
