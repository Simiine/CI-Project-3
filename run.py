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
                    3. Delete Event
                    4. Exit
                    """)

        option = input("Choose options from 1 - 6: ")
        if option == "1":
            add_event()
        elif option == "2":
            display_all_events()
        elif option == "3":
            delete_event()
        elif option == "4":
            exit();
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
    while True:
        start_time = input("Enter the start time: ")
        end_time = input("Enter the end time: ")
        if validate_time(start_time, end_time):
            event_details.append(start_time)
            event_details.append(end_time)
            break
    while True:
        location = input("Enter location: ")
        if validate_data(location):
            event_details.append(location)
            break
    while True:
        description = input("Enter description of event: ")
        if validate_data(description):
            event_details.append(description)
            break
    return update_events_worksheet(event_details)


def validate_data(values):
    """
    Validate to check if string inputs have data
    """
    try:
        if len(values) == 0:
            raise ValueError()
    except ValueError as e:
        print("Empty sting, please fill in. \n")
        return False
    return True


def validate_date(date):
    """
    Validate date to check it is in the right format dd/mm/yy
    """
    try:
        if datetime.datetime.strptime(date, '%d-%m-%Y') is False:
            raise ValueError()
        
        try:
            if datetime.datetime.strptime(date, '%d-%m-%Y') < datetime.datetime.now():
                raise ValueError()
        except ValueError as e:
            print("Error: Date is earlier than current date. Input date again. \n")
            return False

    except ValueError as e:
        print("Incorrect data format, should be DD-MM-YYYY.\n")
        return False
    return True


def validate_time(start_time, end_time):
    """
    Validate start and end time to check it is in the right format 12-hour time
    """
    try:
        if datetime.datetime.strptime(start_time, '%I:%M %p') is False:
            raise ValueError()
        elif datetime.datetime.strptime(end_time, '%I:%M %p') is False:
            raise ValueError()
        try:
            if datetime.datetime.strptime(start_time, '%I:%M %p') > datetime.datetime.strptime(end_time, '%I:%M %p'):
                raise ValueError()
        except ValueError as e:
            print("Error: Start time is later than you end time. Input time again.\n")
            return False
            
    except ValueError as e:
        print("Incorrect time format, should be 12-hour time ")
        return False
    return True

def update_events_worksheet(event): #event_details #data
    """
    Update events worksheet, add a new row with new event added
    """
    print("Updating Events Planner...\n")
    events_worksheet = SHEET.worksheet("events")
    events_worksheet.append_row(event) #add_events #events_details
    print("Events Planner updated successfully.\n")


# def update_events_worksheet(add_event):
#     """
#     Update events worksheet, add a new row with the data list provided.
#     """
#     print("Updating events planner...\n")
#     events_worksheet = SHEET.worksheet("events")
#     events_worksheet.append_row(events_details)
#     print("Event successfully added to planner.")

def display_all_events():
    """
    Function to get all the events from the Google sheet and display them in the terminal
    """
    all_events = EVENTS.get_all_records()
    if all_events:
        for events in all_events:
            print_all_events(events)
    else:
        print("No events in planner")

def print_all_events(existing):
    """
    Displays all the events 
    """
    event = []
    print("-----")
    print("-----")
    for key, value in existing.items():
        print(f'{key}: {value}')
    return event
    print("-----")
    print("-----")


    # all_events = EVENTS.get_all_values()
    # if all_events:
    #     for events in all_events:
    #         print_all_events(events)
    # else:
    #     print("No events in planner")

    

menu()

