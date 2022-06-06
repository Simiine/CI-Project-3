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
menu()
