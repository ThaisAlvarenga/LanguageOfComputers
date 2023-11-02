'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers

DESCRIPTION: Simple Word Game. Game in which user tries to guess the secret word already assigned to the program.

DATE: 01/02/2023

'''

# assign a secret word
secretWord = "memory"

# prompt user input
userGuess = input("Welcome to the Simple Word Game. Guess the secret word to win a prize! \n Your guess: ")

# check input
print("You're guessing the word:", userGuess)

# check if userGuess is the same as the secretWord
if (userGuess == secretWord):
    print("CONGRATS! You win One million Falcon Dirhams")
    
# check loosing condition
else:
    print("Sorry! You lost the game!")
