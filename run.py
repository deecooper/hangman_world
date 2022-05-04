import random


 # https://www.youtube.com/watch?v=5x6iAKdJB6U

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
        chances = len(word) + 2
        correct = 0
        is_correct = False

    try:
        while (chances != 0) and is_correct = False:
            print("enter another letter")
            chances -= 1

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
                    letter guessed += guess

            #print the word
            for char in word:
                if char in letters_guessed and (Counter(letters_guessed)) != Counter(word)):
                    print(char, end ' ')
                    correct += 1
                elif (Counter(letters_guessed)) == Counter(word)):
                    print('The word is: ', end = ' ')
                    print(word)
                    is_correct = True
                    play_again()
                    break
                    break
                else:
                    print('_', end = ' ')

        # Player has ran out of chances

        if chances <= 0 and (Counter(letter_guessed) != Counter(word)):
            print()
            print('You lost loser')
            print(f'The word was {word}')
            play_again()
    
    except KeyboardInterrupt:
        print('Bye bye')
        exit()








def hangman_word(word_choice):
    #https://www.youtube.com/watch?v=m4nEnsavl6w
    """
    This function return the word as underscores for the user to guess the word
    """
    
    word_completion = "_" * len(word_choice)
    guessed = False
    letters_guessed = []
    words_guessed = []
    guessmade = ''
    tries = 9
    print("Lets Play")
    print("----------------------")
    print(word_completion)
    print("-----------------------")
    print(hangman_stages(tries))
    #https://www.youtube.com/watch?v=WZZ9pY-cP2s
    while not guessed and tries > 0:
        guess = input("please guess a letter or word").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in letters_guessed:
                print(f"You have already guessed this letter + {guess}")
            elif guess not in word_choice:
                print(f"This letter is not in the word {guess}")
                tries -= 1
                letters_guessed.append(guess)
            else:
                print(f"Well done {guess} is in the word")
                letters_guessed.append(guess)
                word_list = list(word_completion)
                indices = [i for i, letter in enumerate(word_choice) if letter == guess]
                for index in indices:
                    word_list[index] = guess
                word_completion = "".join(word_list)
                if "_" not in word_completion:
                    guessed = True
        elif len(guess) == len(word_choice) and guess.isalpha():
            if guess in words_guessed:
                print(f"You already guessed the word {guess}")
            elif guess != word_choice:
                print(f"{guess} is not in the word")
                tries -= 1
                words_guessed.append(guess)
            else:
                guessed = True
                word_completion = word_choice
        else:
            print("Guess is not valid try again")
            print(hangman_stages(tries))
            print(word_completion)
            print("\n")
    if guessed:
        print("Well done you guessed the word")
    else:
        print(f"sorry you ran out of tries the word was {word_choice}")


def hangman_stages(tries):
    hangman_icons = ['''
      -------
      |     |
      |     |
      |     O
      |    \|/
      |    / \\
      |
    ----- ''' , '''
      -------
      |     |
      |     |
      |     O
      |    \|/
      |    /
      |
    ----- ''' , '''
    
      -------
      |     |
      |     |
      |     O
      |    \|/
      |
      |
    ----- ''' , '''

      -------
      |     |
      |     |
      |     O
      |     |/
      |
      |
    ----- ''' , '''
      -------
      |     |
      |     |
      |     O
      |     |
      |
      |
    ----- ''', '''
      -------
      |     |
      |     |
      |     O
      |
      |
      |
    ----- ''' , '''
      -------
      |     |
      |     |
      |
      |
      |
      |
    ----- ''' , '''
      ------- 
      |     |
      |
      |
      |
      |
      |
    ----- ''', '''
      ------- 
      |     
      |
      |
      |
      |
      |
    ----- '''
    ]
    return hangman_icons(tries)
    



    



def welcome_msg():
    """
    This function allows users to enter their name into the input field
    """
    name = input("Enter your name:  ")
    print(f"Hello {name} welcome to Hangman World")
    print("----------------------------")
    play_game()



    
    #try statement here for strings






def welcome():
    """
    This function gives the user the option to play the game,
    read instructions, look at the high scores and exit the game
    """
    while True:
        welcome_msg = "Hello and welcome to Hangman\
        World please select one of the following \
        options by typing a number. Type 1 for play game, \
        2 for instructions, 3 for High Scores and 4 for exit " 
        print(welcome_msg)
        print("_______________________________________")
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
            word = get_word()
            break
        elif start_choice == "2":
    
            print("Hangman World is a word guessing game and as the\
            name suggests the player will be asked to guess the name of the\
            place in the world which the computer has chosen. The player will\
            have eight attempts to guess the word before they are hanged. Good Luck!")
        elif start_choice == "3":
            print(data)
        elif start_choice == "4":
            print("quitting game bye")
            sys(exit)
        else:
            print("you have not choose one of the selections\
            please try again")

            #try statement for anything that isnt 1,2,3,4 and isnt a number

    

welcome()
