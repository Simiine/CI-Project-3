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
    Display menu with a list of options to choose from
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

        option = input("Choose options from 1 - 4: ")
        if option == "1":
            add_event()
        elif option == "2":
            display_all_events()
        elif option == "3":
            delete_event()
        elif option == "4":
            exit_programme()
        else:
            print("Invalid option, please select number from 1 - 4: ")


def add_event():
    """
    Adds a new event to the excel file with the following information
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
    Validate the date to check it is in the right format dd/mm/yy
    """
    try:
        if datetime.datetime.strptime(date, '%d-%m-%Y') is False:
            raise ValueError()
        try:
            if datetime.datetime.strptime(date, '%d-%m-%Y') < datetime.datetime.now():
                raise ValueError()
        except ValueError as e:
            print("Error: Date is earlier than current date.\n"
                  "Input date again. \n")
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
            print("Error: Start time is later than your end time.\n"
                  "Input start and end time again.\n")
            return False
    except ValueError as e:
        print("Incorrect time format.\n"
              "should be 12-hour time (e.g. 2:00 pm)")
        return False
    return True


def update_events_worksheet(event):
    """
    Update events worksheet, adding a new row with a new event added
    """
    print("Updating Events Planner...\n")
    events_worksheet = SHEET.worksheet("events")
    events_worksheet.append_row(event)
    print("Events Planner updated successfully.\n")


def display_all_events():
    """
    Function to get all the events from the Google sheet
    and display them in the terminal
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


def delete_event():
    """
    Delete an event from the Google sheet
    """
    while True:
        name = input("Please enter the name of the event: ")
        event = EVENTS.col_values(1)
        if name in event:
            rownum = event.index(name) + 1
            row = EVENTS.row_values(rownum)
            headings = EVENTS.row_values(1)
            search = dict(zip(headings, row))
            for key, value in search.items():
                print(f'{key}: {value}')
            print("Deleting event from planner...\n")
            EVENTS.delete_rows(rownum)
            print("Event has been deleted. \n")
            break
        else:
            print("Error: no event with that title.\n"
                  "Please enter valid title.\n")


def exit_programme():
    """
    Exit from programme
    """
    print("Exiting programme...\n")
    print("--------Thank you for using this programme--------")
    print("--------------------Goodbye-----------------------\n")
    exit()
menu()
