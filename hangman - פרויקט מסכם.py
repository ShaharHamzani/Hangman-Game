def animate(MAX_TRIES):

    """
    This function prints the "loading" animation to the terminal
      and calls the func "print_start_screen()" to print the start screen

    :param MAX_TRIES
    :type int
    :return: none
    :rtype: none
    """

    done = False
    load_count = 0
    

    while done == False:
        sys.stdout.write('\rloading game.')
        time.sleep(0.2)
        sys.stdout.write('\rloading game..')
        time.sleep(0.2)
        sys.stdout.write('\rloading game...')
        time.sleep(0.2)
        sys.stdout.write('\rloading game   ')
        time.sleep(0.2)
        load_count +=1
        if load_count == 3:
            sys.stdout.write('\rStarting game in: 3')
            time.sleep(1)
            sys.stdout.write('\rStarting game in: 2')
            time.sleep(1)
            sys.stdout.write('\rStarting game in: 1')
            time.sleep(1)
            sys.stdout.write('\rStarting game in: 0')
            time.sleep(1)
            sys.stdout.write('\r                   ')

            play_sound(r"C:\Users\shaha\OneDrive\מסמכים\קבצים חשובים\vs codes\קורס פייתון\hangman\music sounds\01. Ground Theme.mp3")

            sys.stdout.write(print_start_screen(MAX_TRIES))
            input("\n\t\tPress Enter to start: ")
            mixer.music.stop()
            done = True



def play_sound(sound_file_path):

    """
    This function plays the sound from the file path given as an argument 

    :param sound_file_path
    :type str
    :return: none
    :rtype: none
    """

    mixer.init()
    mixer.music.load(sound_file_path)
    mixer.music.play()



def choose_word(file_path, index):

    """
    This function returns a word at the position received
    as an argument to the function (index),
    (from the file received as an argument(file_path))
    which will be used as the secret word for guessing.

    :param file_path
    :type str
    :param index
    :type int
    :return: secret_word
    :rtype: str
    """

    with open(file_path,"r") as file_obj:
        file_data = file_obj.read()
        file_data = file_data.replace("\n", " ")
        file_data = "".join(file_data).split("\t")
        file_data = "".join(file_data).split(" ")
 



    while len(file_data) < index:
        index = index - len(file_data)

    secret_word = file_data[index-1]       

    return secret_word



def check_win(secret_word, old_letters_guessed):

    """
    The function returns true if all the letters that make
    up the secret word are included in the list of letters
    that the user guessed (old_letters_guessed). Otherwise, the function returns false.

    :param secret_word: The secret word
    :param old_letters_guessed: The already guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False
    :rtype: boolean
    """

    guessed_letters_in_board = "_" * len(secret_word)
    guessed_letters_in_board = list(guessed_letters_in_board)

    for item in old_letters_guessed:
        for i in range(len(secret_word)):
            if secret_word[i] == item:
                 guessed_letters_in_board[i] = item
                

    guessed_letters_in_board = ''.join(guessed_letters_in_board)
    

    return (secret_word == guessed_letters_in_board)

    


def show_hidden_word(secret_word, old_letters_guessed):

    """
    This function returns the guessed letters 
    inside the game board using the secrat word
    and the old guessed letters.

    :param secret_word: The secret word
    :param old_letters_guessed: The already guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: guessed letters inside the game board.
    :rtype: str
    """

    guessed_letters_in_board = "_" * len(secret_word)
    guessed_letters_in_board = list(guessed_letters_in_board)

    for item in old_letters_guessed:
        for i in range(len(secret_word)):
            if secret_word[i] == item:
                 guessed_letters_in_board[i] = item
                

    guessed_letters_in_board = ' '.join(guessed_letters_in_board)
    return guessed_letters_in_board



def check_valid_input(letter_guessed, old_letters_guessed):
    """
    This function returns True if the guessed latter is 
    made of one key, is a latter from the English alphabet 
    and if it wasen't already guessed by the player.
    If not, the function will return False.

    :param letter_guessed: The guessed latter
    :param old_letters_guessed: The already guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False.
    :rtype: boolean
    """

    letter_guessed = letter_guessed.lower()

    return (len(letter_guessed) == 1 and 
               letter_guessed.isalpha() and 
               old_letters_guessed.count(letter_guessed) == 0)





def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    This function returns True if the guessed latter is 
    correct for the game and False if it is not.
    when it returns False it also prints the letter 'X'
    and the string (string_old_letters_guessed)
    If not, the function will return True.

    :param letter_guessed: The guessed latter
    :param old_letters_guessed: The already guessed letters
    :type letter_guessed: str
    :type old_letters_guessed: list
    :return: True/False.
    :rtype: boolean
    """
    
    if check_valid_input(letter_guessed, old_letters_guessed) == True:
        old_letters_guessed.append(letter_guessed.lower())
        return True
    
    else:
        old_letters_guessed.sort()
        string_old_letters_guessed = " -> ".join(old_letters_guessed)
        string_old_letters_guessed.lower()
        print("X", "\n", string_old_letters_guessed)
        return False
    


def print_start_screen(MAX_TRIES):

    """
    This function prints the start screen of the game to the terminal 

    :param none
    :type none
    :return: none
    :rtype: none
    """

    clean_screen()

    HANGMAN_ASCII_ART = """\n\t\tWelcome to the game Hangman\n     _    _                                         
    | |  | |                                        
    | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
    |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
    | |  | | (_| | | | | (_| | | | | | | (_| | | | |
    |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                      
                        |___/\n%d"""
    


    return HANGMAN_ASCII_ART % MAX_TRIES



def print_hangman(num_of_tries):

    """
    The function prints one of the seven states of the hanging man, using:
    ~ a variable called num_of_tries(int) that displays the number of failed attempts by the user so far.
    ~ The dict HANGMAN_PHOTOS  

    :param num_of_tries
    :type int
    :return: HANGMAN_PHOTOS[?]
    :rtype: str
    """
    

    HANGMAN_PHOTOS = {0 :  """    x-------x""", 1 : """    x-------x
    |
    |
    |
    |
    |""", 2 : """    x-------x
    |       |
    |       0
    |
    |
    |""", 3 : """    x-------x
    |       |
    |       0
    |       |
    |
    |""", 4 : """    x-------x
    |       |
    |       0
    |      /|\\
    |
    |""", 5 : """    x-------x
    |       |
    |       0
    |      /|\\
    |      /
    |""", 6 : """    x-------x
    |       |
    |       0
    |      /|\\
    |      / \\
    |"""}


    return "That is your currnt state:\n" + HANGMAN_PHOTOS[num_of_tries]



def clean_screen():

    """
    This function clears the terminal 

    :param none
    :type none
    :return: none
    :rtype: none
    """

    os.system('cls||clear')


def win():

    """
    This function makes a "win" animation 

    :param none
    :type none
    :return: none
    :rtype: none
    """

    # Define the frames for the animation
    frames = [
        "W   W IIIII N   N",
        "W W   I   NN  N",
        "W W   I   N N N",
        "W W   I   N  NN",
        " W    I   N   N"
    ]

    # Display the frames in a loop
    while True:
        for frame in frames:
            print("\r" + frame, end='')
            time.sleep(0.2)



def lose():

    """
    This function makes a "lose" animation 

    :param none
    :type none
    :return: none
    :rtype: none
    """

    # Define the frames for the animation
    frames = [
        "L   O   S   E",
        "L  O O  S S  E",
        "L O   O S     E",
        "L O   O  S    E",
        "L O   O   S   E",
        "L  O O     S  E",
        "L   O   S   E"
    ]

    # Display the frames in a loop
    while True:
        for frame in frames:
            print("\r" + frame, end='')
            time.sleep(0.5)  # Adjust the delay as needed





import time
import sys
import random
import os
from pygame import mixer




def main():

    

    clean_screen() # clean the screen

    # Get the file path from the user
    file  = input("Enter the file path: ").strip()
    file = file.replace('"', "")
    print("The file path has been saved")
    time.sleep(1)

    # Read the contents of the file and process it
    with open(file,"r") as file_obj:
        # Remove newline characters and split the data
        file_data = file_obj.read()
        file_data = file_data.replace("\n", " ")
        file_data = "".join(file_data).split("\t")
        file_data = "".join(file_data).split(" ")

    # Determine the length of the data and choose a random word
    legth = len(file_data)
    index_num = random.randint(1,legth) # rundomize a number to choose a word randomly. (Randomly choose an index)
    secret_word = choose_word(file, index_num)
    


    # Set the maximum number failed of tries for the hangman game
    MAX_TRIES = 6

    # Start "loading" animation
    animate(MAX_TRIES)

    
    # Initialize variables for tracking progress
    num_of_tries = 0
    old_letters_guessed = []

    clean_screen() # clean the screen

    # Display the initial hangman and hidden word states
    print(print_hangman(num_of_tries))
    print(show_hidden_word(secret_word, old_letters_guessed))


    
    # Main game loop
    while check_win(secret_word, old_letters_guessed) != True and num_of_tries != MAX_TRIES:
        letter_guessed = input("Enter a letter: ")
        while try_update_letter_guessed(letter_guessed, old_letters_guessed) == False:
            letter_guessed = input("Enter a new letter: ")
        else:
            if letter_guessed in list(secret_word):
                # Correct guess: update display and show progress
                clean_screen() # clean the screen
                print("(:")
                
                # play the correct guess sound
                play_sound(r"C:--path--\music sounds\good gusse.mp3")

                print("Num of failed tries left: ", MAX_TRIES - num_of_tries)

                print(print_hangman(num_of_tries))
                print(show_hidden_word(secret_word, old_letters_guessed))
            else:
                # Incorrect guess: update display and increment feiled tries
                clean_screen() # clean the screen
                print("):")
                
                # play the incorrect guess sound
                play_sound(r"C:--path--\music sounds\bad gusse.mp3")

                num_of_tries+=1
                print("Num of failed tries left: ", MAX_TRIES - num_of_tries)

                print(print_hangman(num_of_tries))
                print(show_hidden_word(secret_word, old_letters_guessed))

            print(old_letters_guessed)

            # Check for win or loss or continue the game
            if check_win(secret_word, old_letters_guessed) == True:
                print("WIN!!!")
                
                # play the wining sound
                play_sound(r"C:--path--\music sounds\win.mp3")

                win()
            elif num_of_tries == MAX_TRIES:
                print("LOSE..\n     ^")
                print("The word was :", secret_word)

                # play the losing sound
                play_sound(r"C:--path--\music sounds\game over.mp3")

                lose()
            



if __name__ == "__main__":
    main()