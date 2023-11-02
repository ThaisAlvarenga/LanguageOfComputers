'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Guess the secret random word from a list of words in a file
DATE: 24/02/2023

'''

import random

# function to read a file 
def readFile(filename):

    # open file for read
    mywords = open(filename, "r")

    # for each line in file
    for line in mywords:

        # clean the line
        line = line.rstrip()
        # append the line to word list
        words.append(line)
        
    # print words just to check    
    #print(words)

    # close file
    mywords.close()
    
# end readFile

def checkGuess(guess, secretWord):

    # check if guess is correct
    if guess == secretWord:
        print("Congratulations! You guessed the secret word.")
    else:
        print("Sorry, you lost. The secret word was", secretWord)
# end of guess



# declare list of words
words = []



def main():

    # assign variable to read words 
    filename = "files/words.txt"

    # read file and populate word list
    readFile(filename)

    # choose a random word
    secretWord = random.choice(words)

    # ask user to guess the word
    guess = input("Guess the secret word: ")

    # check user guess and output wether correct or not
    checkGuess(guess, secretWord)

    
# end of main

main()
