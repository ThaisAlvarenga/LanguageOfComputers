'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generate 100 numbers randomly between (1 and 1000000) and computes the max and min. 
DATE: 14/02/2023
'''


#add modules to program
import random



# function to set the starting values of variables required for program
def initializeVariables():
    # initialize a variable to run the program
    runProgram = 0

    # declare variables to track max and min
    maximum = 0;
    minimum = float('inf')

    return runProgram, maximum, minimum

# end of initializeVariables()



# function to get maximum number of the generated list
def getMax(currentNum, maxNum):
    
    # if currentNum generated is bigger than the maximum value
    if(currentNum > maxNum):
        
        # set the maximum to that of currentNum
        maxNum = currentNum

    # return the new maximum number            
    return maxNum

# end of getMax()



# function to get minimum number of the generated list
def getMin(currentNum, minNum):
    
    # if num generated is smaller than the minimum value
    if( currentNum < minNum ):
        # set the minimum to the generated num
        minNum = currentNum

    # return the new minimum number
    return minNum

# end of getMax()



def main():
    # initialize a variable to run the program
    runProgram, maximum, minimum = initializeVariables()

    # while user chooses not to exit program
    while (runProgram != -1):

        for num in range(100):
            num = random.randint( 1, 1000000 )

            print('num generated:', num)

                
            # get the maximum of the generated numbers 
            maximum = getMax(num,maximum)
            minimum = getMin(num,minimum)

        print()

        #print the max and min of the generated numbers
        print("Max: ", maximum)
        print("Min: ", minimum)

        # get user input to repeat or exit the program
        runProgram = int(input("enter -1 to stop entering data, else input any number: "))
        
# end of main()


main()
