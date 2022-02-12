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
SHEET = GSPREAD_CLIENT.open('household_game')

def get_games_data():
    """
    Get games information input from the user.
    Run a while loop to collect a valid string of data from the user
    via the terminal, which must be a string of 6 numbers separated
    by commas. The loop will repeatedly request data, until it is valid.
    """
    while True:
        print("Please enter game data information into console.")
        print("Data should be six numbers, separated by commas.")
        print("Example: 10,20,30,40,50,60\n")

        data_str = input("Enter your data here:\n")

        games_data = data_str.split(",")

        if validate_data(ganes_data):
            print("Data is valid!")
            break

    return games_data


def submit_game():

    """
    Call email, username, and game_info functions one by one

    This function handles the automated python email sent to user

    The email is sent from household game to the user email given.

    As it is an automatic email, it is the user's responsibility

    to enter valid information.

    The credits of raw-python email code is mentioned in README.md
    """

global USER_EMAIL
global FULL_NAME
global GAME_DATA
global HOURSPLAYED_DATA
global GENRE_DATA
global CONSOLE_DATA
global STARRATING_DATA
USER_EMAIL = email()
FULL_NAME = username()
print(FULL_NAME)
GANE_DATA = game_info()
print(GAME_DATA)
HOURSPLAYED_DATA = hours_played_data()
print(HOURSPLAYED_DATA)
CONSOLE = console_data()
print(CONSOLE_DATA)
GENRE_DATA = genre_data()
print(GENRE_DATA)
STARRATING_DATA = star_rating_data()
print(STARRATING_DATA)