import random
# Love Sandwiches
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
SHEET = GSPREAD_CLIENT.open('high_scores_hangman')


high_scores = SHEET.worksheet('highscores')

data = high_scores.get_all_values()


 # https://www.youtube.com/watch?v=5x6iAKdJB6U

def get_word():
    """
    This function gets the random word from the words.txt file"""
    with open("words.txt", "r") as f:
        word = f.readlines()
    word_choice = random.choice(word)
    return word_choice.upper()
    #random_word = get_word()
    #print(random_word)

def hangman_word(word_choice):
    #https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    This function return the word as underscores for the user to guess the word
    """
    word_completion = "_" + len(word_choice)
    guessed = False
    letters_guessed = []
    words_guessed = []
    tries = 8
    print(tries)
    print(word_completion)

def play_game():
    name = input("input your name:  ")
    print(f"Hello {name} welcome to hangman world")
    get_word()



def welcome():
    """
    This function gives the user the option to play the game,
    read instructions, look at the high scores and exit the game
    """
    while True:
        welcome_msg = "Hello and welcome to Hangman\
        World please select one of the following \
        options by typing in the number beside your\
        selection into the answer field" 
        print(welcome_msg)
        play = "1. Play Game"
        print(play)
        instructions = "2. Instructions"
        print(instructions)
        high_scores = "3. High Scores"
        print(high_scores)
        quit ="4. Quit"
        print(quit)
        start_choice = input("Enter your answer here 1,2,3,4: ")
        if start_choice == "1":
            
            print("You have choose play game")
            play_game()
            break
        elif start_choice == "2":
    
            print("Hangman World is a word guessing game and as the\
            name suggests the user will be asked to guess the name of the\
            place in the world which the computer has chosen")
        elif start_choice == "3":
            print(data)
        elif start_choice == "4":
            print("quitting game bye")
        else:
            print("you have not choose one of the selections\
            please try again")

    

welcome()




    