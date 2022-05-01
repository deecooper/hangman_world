# Love Sandwiches
import gspread
import random
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('high_scores_hangman')


high_scores = SHEET.worksheet('highscores')

data = high_scores.get_all_values()
print(data)
 # https://www.youtube.com/watch?v=5x6iAKdJB6U

def get_word():
    with open("words.txt", "r") as f:
        word = f.readlines()
    word_choice = random.choice(word)
    return word_choice
  


random_word = get_word()
print(random_word)
