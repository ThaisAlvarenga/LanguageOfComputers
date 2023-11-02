'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Gives the user 2 opportunities to guess a secret number
selected randomly within the range between 1000 and 100000. 
DATE:07/02/2023
'''
# import random module
import random

# generate a secret numner between 1000 and 100000
secretNumber = random.randint(1000,100000)

# print instructions
print('Welcome to the Guess The Number Game!')
print('You have 2 trials to guess the secret number')

# initialize count variable for while loop
numTrial = 0

# while user still has trials
while (numTrial < 2):
    # get user's guess number and assign it to a variable
    userGuess = int(input('Guess a secret number between 1000 and 100000: '))

    # check if the user guessed the number
    if(secretNumber == userGuess):
        print("Congrats! You won the game!")
        # break out of the loop
        break
    # check if user is not in their last trial
    if(numTrial < numTrial - 1):
        print("Sorry, that's not the number. Try again")
    #add 1 to the number of trials 
    numTrial += 1

# check for loosing condition
if(secretNumber != userGuess):
    #print that user lost
    print("Sorry, you've used all your trials. You lost.")
