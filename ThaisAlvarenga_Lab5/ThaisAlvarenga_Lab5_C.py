
'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Draws a box according to user's input of width, height and character

**********
*        *
*        *
*        *
**********

DATE: 14/02/2023
'''

# function to get user input for box parameters
def getUserInput():
    # ask user for width, height and character to draw the  box
    setWidth = int(input("Enter the width of the box: "))
    setHeight = int(input("Enter the height of the box: "))
    setChar = input("Enter the character to draw the box: ")

    # return the input values
    return setWidth, setHeight, setChar

# end of getUserInput()


# function to draw the top and bottom of the box
def boxTopBottom(myChar, myWidth):
    
    # print a line using myChar that is the length of myWidth
    print(myChar*myWidth)
    
# end of boxTop()


# function to draw the sides of the box
def boxSides(myChar, myWidth, myHeight):

    # for every row in the box
    for row in range(myHeight-2):

        # print first character of left side
        print(myChar, end = "")

        # print space in between sides
        print(" " * ( myWidth - 2 ), end="")
        
        # print the last character for the side
        print(myChar)
            
        
        
# end of boxSides()


# function to draw the whole box
def drawBox(myChar, myWidth, myHeight):

    # draw the top of the box
    boxTopBottom(myChar,myWidth)
    
    # draw the sides of the box
    boxSides(myChar, myWidth, myHeight)
    
    # draw the bottom of the box
    boxTopBottom(myChar,myWidth)

# end of drawBox()



def main():

    # set varaibles to user input
    width, height, char = getUserInput()

    # have a space between input and output
    print()

    # draw the box according to user input
    drawBox(char, width, height)
    
# end of main   



main()
