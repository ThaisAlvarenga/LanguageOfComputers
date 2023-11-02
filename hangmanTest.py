import random
import requests

numOfTries = 12


def get_word():
   
    url = 'https://cs.nyu.edu/~odeh/resources/python/animals.txt'
    response = requests.get(url)
    words = response.text.split()
    return random.choice(words).lower()

def display_word(word, guesses):

    result = ''
    
    for letter in word:
        if letter in guesses:
            result += letter
        else:
            result += '_'
        result += ' '
    return result


def draw_stickman(num_wrong):
##    """
##    This function takes the number of wrong guesses as input and prints a stick figure of a hangman.
##    """
##    if num_wrong == 0:
##        print("  ________     ")
##        print(" |/       |    ")
##        print(" |             ")
##        print(" |             ")
##        print(" |             ")
##        print(" |             ")
##    elif num_wrong == 1:
##        print("  ________     ")
##        print(" |/       |    ")
##        print(" |       (_ )  ")
##        print(" |             ")
##        print(" |             ")
##        print(" |             ")
##    elif num_wrong == 2:
##        print("  ________     ")
##        print(" |/       |    ")
##        print(" |       (_ )  ")
##        print(" |        |    ")
##        print(" |             ")
##        print(" |             ")
##    elif num_wrong == 3:
##        print("  ________     ")
##        print(" |/       |    ")
##        print(" |       (_ )  ")
##        print(" |        |    ")
##        print(" |        |    ")
##        print(" |             ")
##    elif num_wrong == 4:
##        print("  ________     ")
##        print(" |/       |    ")
##        print(" |       (_ )  ")
##        print(" |        |    ")
##        print(" |        |    ")
##        print(" |       /     ")
    if num_wrong == 5:
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|                [X—X]")
        print("|                  |")
        print("|                 /|\\")
        print("|                  |")
        print("|                 | |")
        print("|")
        print("|\_")



def play_hangman():
    """
    This function allows the user to play a game of hangman.
    """
    word = get_word()
    guesses = set()
    num_wrong = 0
    max_wrong = 5
    
    print("Let's play Hangman!")
    print(f"The word has {len(word)} letters.")
    
    while True:
        print(display_word(word, guesses))
        letter = input("Guess a letter: ").lower()
        if letter in guesses:
            print("You already guessed that letter. Try again.")
        else:
            guesses.add(letter)
            if letter in word:
                print(f"Good guess! '{letter}' is in the word.")
            else:
                print(f"Sorry, '{letter}' is not in the word.")
                num_wrong += 1
                draw_stickman(num_wrong)
            
        if num_wrong == max_wrong:
            print("You lose! The word was:", word)
            break
        elif set(word) == guesses:
            print("Congratulations! You guessed the word:", word)
            break

play_hangman()

