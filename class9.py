'''
Description: Data scrapint from the web


1. Allow users to view files
2. allow developer to store files/programs
3. allow user to execute programs

IP Address -> a unique twelve set number given as the address of a machine/computer
(like a PO Box but for your files in the internet)

Internet -> infrastructure that allows you to request for a file

http -> the protocol to link the server with the file

Server -> if it finds the file, it says ok, sends the type of the file and then sends a copy of the file
Error 404 is when the file is not found. Error 403, is a permission error, file is there but the
developer didn't give permission for the client to read it

Server programs output html pages, but have programs that run first. example: javascript, php, etc

Servers and databases are always private.

Socket communication -> communicating with a machine, telling it the program

Binary files -> like html, csv etc, have markup or metadata that describe the data based on style
'''


# to get an html file from the web

import requests
import random

words = []

def getHTMLFileFromWeb():
    url = "https://www.nytimes.com"

    response = requests.get(url)

    # print out the property that has the text
    # it's basically going to print the html document
    print(response.text)
    
# end of getHTMLFileFromWeb()



def getTEXTFileFromWeb():
    # define url

    url = "https://cs.nyu.edu/~odeh/resources/python/animals.txt"

    response = requests.get(url)

    #print(response.text)

    # converts from binary to a string
    text = response.content.decode("UTF-8")

    print(text)

    words = text.split("\n")

    print(words, "\n")

    return words

# end of getTEXTFileFromWeb()



def checkGuess(guess, secretWord):

    # check if guess is correct
    if guess == secretWord:
        print("Congratulations! You guessed the secret word.")
    else:
        print("Sorry, you lost. The secret word was", secretWord)
        
# end of checkGuess()
    


def main():

    #getHTMLFileFromWeb()

    # read file as text from web
    words = getTEXTFileFromWeb()

    
    randomWord = random.choice(words)

    print(randomWord)

    # ask user to guess the word
    guess = input("Guess the secret word: ")

    # check user guess and output whether correct or not
    checkGuess(guess, randomWord)

# end of main() 


main()
