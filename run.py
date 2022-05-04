import random
from collections import Counter

def get_word():
    """ Returns a secret word to guess """
    word_list = """europe america africa australia asia antartica ireland\
         england russia china india japan korea spain"""
    word_list = word_list.split(' ')
    chosen_word = random.choice(word_list)
    return chosen_word


def play_game():
    name = input("Enter your name:  ")
    print(f"Hello {name} welcome to Hangman World")
    print("----------------------------")
    word = get_word()

    for index in word:
        print('_', end = ' ')
        playing = True
        letters_guessed = ''
        chances = len(word) + 3
        correct = 0
        is_correct = False

    try:
        while (chances != 0) and is_correct == False:

            print()
            chances -= 1
            print(f"You have {chances} left")

            try:
                guess = str(input('Enter a letter to guess:  '))
            except:
                print('Only a letter wiseguy')
                continue

            if not guess.isalpha():
                print('Enter a letter!')
                continue
            
            elif guess in letters_guessed:
                print('You already guessed this letter wiseguy!!')
                print(letters_guessed)
                continue

            # guessed letter is correct

            if guess in word:
                letter_appears = word.count(guess)
                for _ in range(letter_appears):
                    letters_guessed += guess

            #print the word
            for char in word:
                if char in letters_guessed and (Counter(letters_guessed) != Counter(word)):
                    print(char, end = ' ')
                    correct += 1
                elif (Counter(letters_guessed) == Counter(word)):
                    print('The word is: ', end = ' ')
                    print(word)
                    is_correct = True
                    play_again()
                    break
                    break
                else:
                    print('_', end = ' ')

        # Player has ran out of chances

        if chances <= 0 and (Counter(letters_guessed) != Counter(word)):
            print()
            print('You lost loser')
            print(f'The word was {word}')
            print('''  
                       ---------
                       |     |
                       |     |
                       |     O
                       |    \|/
                       |    / \\
                       |
                      ----- ''' )
            play_again()
    
    except KeyboardInterrupt:
        print('Bye bye')
        exit()

def play_again():
    """
    This function gives the player the option to play again when their game has finished
    """
    while True:
        print("Would you like to play again?")
        another_game = input("Play Again? (Y/N) ").upper()
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
        welcome_msg = "Hello and welcome to Hangman\
        World please select one of the following \
        options by typing a number. Type 1 for play game,\
        2 for instructions, 3 for exit"
        print(welcome_msg)
        print("_______________________________________")
        play = "1. Play Game"
        print(play)
        instructions = "2. Instructions"
        print(instructions)
        quit ="3. Quit"
        print(quit)
        start_choice = input("Enter your answer here 1,2,3: ")
        
        if start_choice == "1":
            print("You have choose play game")
            play_game()
            break
        elif start_choice == "2":
            print("------------------------------")
            print("\n")
            print("Hangman World is a word guessing game and as the\
            name suggests the player will be asked to guess the name of the\
            place in the world which the computer has chosen. The player will\
            have eight attempts to guess the word before they are hanged. Good Luck!\n")
        elif start_choice == "3":
            print("quitting game bye")
            exit()
        else:
            print("you have not choose one of the selections\
            please try again")

            #try statement for anything that isnt 1,2,3,4 and isnt a number

def main():
    """
    main function to call the welcome function to greet players
    """
    welcome()


if __name__ == "__main__":
    main()

