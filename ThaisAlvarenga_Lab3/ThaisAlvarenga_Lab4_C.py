'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Gives the user 2 opportunities to guess a secret number
selected randomly within the range between 1000 and 100000. 
DATE:07/02/2023
'''
# assign a secret word
secretWord = "dog"

# for every trail (with maximum amount of trials being 3)
for trial in range(3):

    # ask the user for their input
    userGuess = input("Guess the word: ")

    # if they guess the word
    if(userGuess == secretWord):
        
        # print that they won
        print("You won One million dollars!You won One million dollars!")
        
        # break out of the loop
        break
    
    # else if user has used all of their trials
    elif(trial == 2):
        print("Sorry! You lost the game!")

    # else when the user gets it wrong
    else:
        #print that the user is incorrect
        print("Sorry, you're incorrect")
        #print out how many trials they have left
        print("You have", 2- trial, "trials left")



