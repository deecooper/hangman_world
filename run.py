import random
from collections import Counter


def get_word():
    """ Returns a secret word to guess """
    word_list = """europe america africa australia asia antartica
ireland england russia china india japan korea spain italy portugal
france thailand turkmenistan singapore brazil """
    word_list = word_list.split(' ')
    chosen_word = random.choice(word_list)
    return chosen_word


def play_game():
    word = get_word()
    guessed_letters = []

    for index in word:
        print('_', end=' ')
        playing = True
        letters = ''
        chances = len(word) + 3
        correct = 0
        is_correct = False

    try:
        while (chances != 0) and is_correct is False:

            print()
            chances -= 1
            print(f"You have {chances} chances left to guess the word")

            try:
                guess = str(input('Enter a letter to guess:\n'))
            except:
                print('Only a letter wiseguy')
                continue

            if not guess.isalpha():
                print('Enter a letter!')
                continue

            elif guess in letters:
                print('You already guessed this letter wiseguy!!')
                guessed_letters.append(guess)
                print(guessed_letters)

                continue

# guessed letter is correct

            if guess in word:
                letter_appears = word.count(guess)
                for _ in range(letter_appears):
                    letters += guess
                    print('Well done')

# print the word
            for char in word:
                if char in letters and (Counter(letters) != Counter(word)):
                    print(char, end=' ')
                    correct += 1
                elif (Counter(letters) == Counter(word)):
                    print('The word is: ', end=' ')
                    print(word)
                    print('Congratulations')
                    is_correct = True
                    play_again()
                    break

                else:
                    print('_', end=' ')

        # Player has ran out of chances

        if chances <= 0 and (Counter(letters) != Counter(word)):
            print()
            print('You lost You have been hanged!!!')
            print(f'The word was {word}')
            print('''
                       |     |
                       |     |
                       |     O
                       |    \|/
                       |    / \\
                       |
                      ----- ''')
            play_again()

    except KeyboardInterrupt:
        print('Bye bye')
        exit()


def name():
    """
    This function allows users to input their name it also calls
    the play game function
    """
    name = input("Enter your name:\n")
    print(f"Hello {name} welcome to Hangman World")
    print("Lets Begin!")
    print("-------------------------------------------")
    play_game()


def play_again():
    """
    This function gives the player the option to play
    again when their game has finished
    """
    while True:
        print("Would you like to play again?")
        another_game = input("Play Again? (Y/N)\n").upper()
        if another_game == "Y":
            play_game()
            break
        elif another_game == "N":
            exit()
            break
        elif not another_game.isalpha():
            print('You must type in y or n')
        else:
            print('You must type in y or n')


def welcome():
    """
    This function gives the user the option to play the game,
    read instructions, look at the high scores and exit the game
    """

    while True:
        welcome_msg = """
-----------------Hangman World-----------------

Hello and welcome to Hangman World please select one of
the following options by typing a number (1,2,3)
Type 1 to start the game, 2 for the Instructions
and 3 to exit the game
        """
        print(welcome_msg)
        print("-----------------------------------------------")
        play = "1. Play Game"
        print(play)
        instructions = "2. Instructions"
        print(instructions)
        quit = "3. Quit"
        print(quit)
        start_choice = input("Enter your answer here 1,2,3:\n")

        if start_choice == "1":
            print("You have selected Play Game")
            name()
            break
        elif start_choice == "2":
            print("-----------------------------")
            print("\n")
            print("""
-----------------Instructions-----------------

Hangman World is a word guessing game.  As the
name suggests the player will be asked to guess the name of the
place in the world which the computer has chosen. The player will
have many attempts to guess the word before they are hanged.
Good Luck!""")
        elif start_choice == "3":
            print("Quitting game bye")
            exit()
        else:
            print("Wrong input please type in 1,2 or 3")


def main():
    """
    main function to call the welcome function to greet players
    """
    welcome()

if __name__ == "__main__":
    main()
