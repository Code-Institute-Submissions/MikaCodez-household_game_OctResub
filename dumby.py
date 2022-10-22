# ----- EMAIL SETTINGS ----- #
import smtplib  # SMTP protocol client (sending emails)
from email.mime.multipart import MIMEMultipart  # MIME (sending emails)
from email.mime.text import MIMEText  # Multipurpose Internet Mail Extensions
if os.path.exists("env.py"):
    import env  # noqa
MY_ADDRESS = os.environ.get("MY_ADDRESS")
PASSWORD = os.environ.get("PASSWORD")

FULL_NAME = ""
GAME_DATA = ""
USER_EMAIL = ""
START_DATE = ""
END_DATE = ""
GAMER_INFO = []


def get_games_data():
    """
    Call email, username, and game_info functions one by one
    This function handles the automated python email sent to user
 
    The email is sent from household game to the user email given.
 
    As it is an automatic email, it is the user's responsibility
 
    to enter valid information.
 
    The credits of raw-python email code is mentioned in README.md
    """
    print("Welcome to HouseHold Game!")
    '''
    Graphic below from https://www.asciiart.eu/video-games/sonic-the-hedgehog
    '''
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
            "i.e. Email, Game, Genre, Hours played, Star rating\n"
            "Are you ready to start?!!\n"''')

games = SHEET.worksheet('games')

data = games.get_all_values()

print(data)

def submit_games():

    data = input("Enter your data here:\n ")
    print(f"The data provided is {data}")

    update_games_worksheet(data)
    print(type(data))
    returned_data = get_games_data()

 
def update_games_worksheet(data):
    """
    Update the games worksheet, by adding new row with the 
    data provided.
    """
    print("Updating games worksheet...\n")

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
print("updating games worksheet...\n")
games_worksheet = SHEET.worksheet("games")
worksheet_headings = games_worksheet.row_values(1)

games_worksheet.append_row([data])
print(data)


print("Games worksheet updated successfully.\n")


data = get_games_data()
games_data = (worksheet.update)
get_games_data()
update_games_worksheet(returned_data)
