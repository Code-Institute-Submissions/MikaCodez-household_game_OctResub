import os
from os import system, name
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
    Call email, username, and game_info functions one by one
    This function handles the automated python email sent to user
 
    The email is sent from household game to the user email given.
 
    As it is an automatic email, it is the user's responsibility
 
    to enter valid information.
 
    The credits of raw-python email code is mentioned in README.md
    """
    while True:
        print("Welcome to HouseHold Game!")
        print(
                '''          .,
                .      _,'f----.._
                |\ ,-'"/  |     ,'
                |,_  ,--.      /
                /,-. ,'`.     (_
                f  o|  o|__     "`-.
                ,-._.,--'_ `.   _.,-`
                `"' ___.,'` j,-'
                `-.__.,--'"
            "Here you will enter a A record of the games that you played, so that you can
            log and track your favourite games"
            "This will be then printed in a spreadsheet for you and sent over to your email!"
            "Please enter game data"
            "data should be as requested, seperated by commas"
            "i.e. Email, Name, Game, Genre, Hours played, Star rating\n"
            "Are you ready to start?!!\n"''')
        print("Data should be seperated by commas.")
        print("Example: Harry@gmail.com, Harry, Pokemon, RPG, Gba, 30, 5*.")
        

        def get_user_input(prompt):
            return input(prompt)

        def print_out_to_console(value_to_be_printed):
            print(value_to_be_printed)
        email = get_user_input("Input your Email address\n")
        name = get_user_input("Input your Name\n")
        game = get_user_input("Input Game Title\n")
        genre = get_user_input("Input Game genre\n")
        console = get_user_input("Input Game Console\n")
        hours_played = get_user_input("Input gameplay hours\n")
        star_rating = get_user_input("Input Star Rating\n")
        # data_str = input("Enter your data here: ")
        
        games_data = data_str.split(",")
        data_str = get_user_input()
        validate_data(games_data)

        if validate_data(games_data):
            print("Data is valid!")
            break

    return games_data


def validate_data(values):
    """
    Inside the try, conerts all string values into integers.
    Raises ValueError if strings cannot be converted into int,
    or if there are more than 7 values.
    """
    
    try:
        [str(values)for value in values]
        if len(values) != 7:
            raise ValueError(
                f"Exactly 7 values required, you provided {len(values)}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again. \n")
        return False

    return True       

def update_games_worksheet(data):
    """
    Update the games worksheet, by adding new row with the 
    data provided.
    """
    print("Updating games worksheet...\n")
    games_worksheet = SHEET.worksheet("games")
    games_worksheet.append_row(data)
    print("Games workshet updated successfully.\n")

def main():
    """
    Run all program functions
    """
    get_user_input = get_games_data()
    values = get_games_data()
    data = get_games_data()
    games_data = [str(values)for value in data]
    update_games_worksheet(games_data)
    

print("Hey all You Crazy Gamers!")
main()
