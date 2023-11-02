'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generate 10 numbers randomly between (1 and 100) and computes the max and min. 
DATE:08/02/2023
'''

#add modules to program
import random

# initialize a variable to run the program
runProgram = 0

# declare variables to track max and min
maximum = 0;
minimum = float('inf')

# while user chooses not to exit program
while (runProgram != -1):

    for num in range( 10 ):
        num = random.randint( 1,100 )

        print('num generated:', num)

        # if num generated is smaller than the minimum value
        if( num < minimum ):
            # set the minimum to the generated num
            minimum = num
        # if num generated is bigger than the minimum value
        if(num > maximum):
            # set the maximum to that num generated
            maximum = num

    print()

    #print the max and min of the generated numbers
    print("Max: ", maximum)
    print("Min: ", minimum)

    # get user input to repeat or exit the program
    runProgram = int(input("enter -1 to stop entering data, else input any number: "))
