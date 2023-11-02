'''

NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Hangman game with list from local file
DATE: 27/02/2023

'''
import random
import requests


# gets list of words from a file in the web
def readFile(filename):

    # open file for read
    wordFile = open(filename, "r")

    # for each line of txt file
    for word in wordFile:
        # remove any trailing characters from a string
        word = word.rstrip()
        # append word to word list
        wordList.append(word)
       
    # close file
    wordFile.close()
    



def startNewGame(secretWord, wordList, playerGuesses):
    # select a random word from list
    secretWord = random.choice(wordList).lower()
    #print(secretWord)

    # empty player Guess list
    playerGuesses.clear()

    # reset try count
    tryCount = 0

    # set new game to false
    newGame = False

    # print starting message and length of word
    print(f"Let's get started. Your word has {len(secretWord)} letters ")

    return secretWord, newGame



# function displays the state of the word being guessed
def displayWordState(secretWord, playerGuesses):
    # variable to hold the state of the word guess
    wordState = ''

    # for every letter in secret word
    for letter in secretWord:
        
        # if the letter was guessed by the player
        if letter in playerGuesses:
            # add that letter so that it will show as guessed
            wordState += letter
            
        # else just write an empty line
        else:
            wordState += '_'
        # add a space
        wordState += ' '
        
    # print the state of the word
    print("Secret Word: ",wordState)
# end



# draws hangman depending on number of try the player is in
def drawHangman(currentTry):

    if currentTry == 0:
        
        print(" __________________ ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 1:
        
        print(" __________________ ")
        print("|                  |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 2:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 3:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 4:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 5:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|                [X—X]")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 6:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|                [X—X]")
        print("|                  |")
        print("|")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 7:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|                [X—X]")
        print("|                  |")
        print("|                 /|\\")
        print("|")
        print("|")
        print("|")
        print("|\_")

    elif currentTry == 8:
        
        print(" __________________ ")
        print("|                  |")
        print("|                  |")
        print("|                  |")
        print("|                 _|_ ")
        print("|                [X—X]")
        print("|                  |")
        print("|                 /|\\")
        print("|                  |")
        print("|")
        print("|")
        print("|\_")

    # if player lost show whole hangman
    else:
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
        
# end of drawHangman()



# checks user input for if user wants to continue playing
def checkIfPlayAgain(isPlaying, newGame):

    while True:
        
        # ask user to repeat or quit game
        continuePlaying = input("Input y to play again or n to quit: ").lower()

        # if player wants to continue playing
        if(continuePlaying == 'y'):
            # continue playing
            isPlaying = True
            # set new game
            newGame = True
            # get out of loop
            break
                    
        # else exit while loop
        elif(continuePlaying == 'n'):
            # stop playing
            isPlaying = False
            newGame = False
            # get out of loop
            break
        
        # tell user input is invalid and repeat loop
        else:
            print("Invalid input")
        

    return(isPlaying, newGame)
# end of checkIfPlayAgain()




# GLOBAL Variables

# set the number of tries a player can have
numTries = 9

# list to hold the words
wordList = []


def main():
    # variable to keep track of playing state
    isPlaying = True
    
    # keeps of track of whether or not this is a new game 
    newGame = True

    # variable to keep track of amount of times player has tried to guess word
    tryCount = 0

    # keeps track of the letters that the player has guesses
    playerGuesses = []
    
    # string to hold the secret word
    secretWord = ''

    # store name of word file
    filename = "words.txt"
    
    # make a list of words from web
    readFile(filename)
    #print("my word list: ", wordList)


    # welcome message
    print("Welcome to Hangman!")

    # while game is playing
    while isPlaying:

        # if this is a new game
        if newGame == True:
            # initialize variables to start a new game 
            secretWord, newGame = startNewGame(secretWord, wordList, playerGuesses)

        # draw hang man
        drawHangman(tryCount)

        # display how the state of the word (with guesses of user)
        displayWordState(secretWord, playerGuesses)
        print()
        
        # get user input and change letter to lower case
        letter = input("Guess a letter: ").lower()

        # if player inputs the same letter from before
        if letter in playerGuesses:
            print("This letter has already been guessed. Input a different one.")

        # else continue playing
        else:
            # append the letter to the player guesses list
            playerGuesses.append(letter)
            print(playerGuesses)

            # if the letter is in the secret word
            if letter in secretWord:
                # congratulate the user
                print(f"You guesses corectly! Letter {letter} is part of the word. Great job!")
            # else
            else:
                # output that guess was incorrect
                print("Sorry, that letter is not used in the word")
                tryCount += 1
                print("Num of tries left:", numTries - tryCount)

        # if user ran out of tries
        if tryCount == numTries:
            # show hangman
            drawHangman(tryCount)
            
            print()
            
            # print lose message
            print("You lose ;-; . The secret word was:", secretWord)
            # ask user to repeat or quit game
            isPlaying, newGame = checkIfPlayAgain(isPlaying, newGame)

        # if user guessed all the letters in the word
        elif all([letters in playerGuesses for letters in secretWord]):
            # print win message
            print("Congratulations! You win! You guessed the secret word.")
            # ask user to repeat or quit game
            isPlaying, newGame = checkIfPlayAgain(isPlaying, newGame)
            

    # print game over message            
    print("Game Over.")
        
            

main()
