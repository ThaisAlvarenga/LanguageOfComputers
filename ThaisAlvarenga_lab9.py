'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Reads list of words from the web and asks user to
guess the secret random word from the list
DATE: 27/02/2023
'''

import requests
import random

# declare list to store words
words = []


# funciton to read text from a file in the web
def getTEXTFileFromWeb():
    
    # variable to define url
    url = "https://cs.nyu.edu/~odeh/resources/python/animals.txt"

    # make a request from url
    response = requests.get(url)

    # convert from binary to a string
    text = response.content.decode("UTF-8")

    # split text to make a list
    words = text.split("\n")

    # return list
    return words

# end of getTEXTFileFromWeb()



# function to check user guess
def checkGuess(guess, secretWord):

    # check if guess is correct and output message accordingly
    if guess == secretWord:
        print("Congratulations! You guessed the secret word.")
    else:
        print("Sorry, you lost. The secret word was", secretWord)
        
# end of checkGuess()
    


def main():

    # read file as text from web
    words = getTEXTFileFromWeb()
    
    # get random word from the list
    randomWord = random.choice(words)

    #print(randomWord)

    # ask user to guess the word
    guess = input("Guess the secret word: ")

    # check user guess and output whether correct or not
    checkGuess(guess, randomWord)

# end of main() 


main()
