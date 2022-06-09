# Event Planner
This programme is an Event planner that allows users to input key events they have comming up. The planner allows them to input the name of event, the date, start and end times, location and brief description. The programme also allows them the display all their inputted events to get a look of whats upcoming at a glance and delete events that they have attended. 

## UX Design
### User Stories
As a user, I want:
* The programme to be simple to use and understand
* The programme to have clear instructions
* A programme with a simple menu
* A programme with good feedback on my inputs and processing my information
* To be able to easily add my events
* To be able to view all my events at a glance and delete events

### Site Owner Goals
As a the owner of this programme, my goals are to:
* Create a programme that is easy to use and navigate
* Create a programme with clear instructions for the user
* Create a programme that can add events, 
* Create a programme that can delete events 
* Create a programme that can display all events
* Create a programme that interacts with Google Sheets

## Structure
### Flowchart 
Link - https://app.diagrams.net/ 

## Features
### Existing Features
#### Main Menu
The main menu opens up with a welcome message that says "Welcome to your Digital Planner". The menu gives the user 4 options to choose. They are asked to choose options from 1 - 4, inputting the number of the option they want to proceed with.
![Menu Options picture]()

#### Add Event
This menu optio allows user to add their event, adding the event title, date, start time, end time and location. Once they input the details and the different sections of their details are validated with the correct input data the event is added to the google spreadsheet. 
![Add Event picture]()

#### Display All Events
This menu optin allows user to display all the events stored in the database. 
![Add Event picture]()

#### Delete Event
This menu options allows user to delete an event from the database byt first searching the event by title and being asked to confirm that it is the event they would like to delete, then deleting it.
![Delete event picture]()

#### Exit
This menu option allows the user to exit from the programme, displaying the message goodbye and thank you for using. 
![Exit picture]()

### Future Features
* Allow user to edit events they have already added to the database, amending their details.

## Testing
In Terminal
PEP8 - http://pep8online.com/

### Bugs
#### AttributeError: ‘dict’ object has no attribute ‘append’
The main issue that kept occuring here was that the add event function would not run. This was because dictionaries in Python do not provide an append option. To resolve this, in order to be able to append the values as they are entered, I had to use a list instead of a dictionary, changing '{ }' to '[ ]'.

#### TypeError: Object of type function is not JSON serializable
The main issue here was that the excel sheet wouldn't update with the newly added event. This was because I was calling the wrong arguments into the functions for adding events and updating the events worksheet. To resolve this I changed the arguments within the respective functions. 
* update_events_worksheet(event_details)
* Def update_events_worksheet(event) 
* events_worksheet.append_row(event)

#### AttributeError: 'list' object has no attribute 'items'
The main issue here was that the events within the database would not display, when the function was called. This was because I was using the wrong code to "get all values" instead of "get all records". To resolve this I rewrote the code to get all records.  

## Deployment
I deployed this project in Heroky using the following steps:


## Technologies Used
* Python

## Credits
* Creating a menu - [Stack Overflow](https://stackoverflow.com/questions/19964603/creating-a-menu-in-python)
* Validating a date string format - [Stack Overflow](https://stackoverflow.com/questions/16870663/how-do-i-validate-a-date-string-format-in-python)
* Validating time strings - [Datatest - Read the Docs](https://datatest.readthedocs.io/en/stable/how-to/date-time-str.html)
* Append values - [Stack Overflow](https://stackoverflow.com/questions/48234473/python-attributeerror-dict-object-has-no-attribute-append)

## Support
* Richard Wells Code Institute Mentor.