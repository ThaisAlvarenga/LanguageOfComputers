# Set the number of rows and columns for the overall output
myRow = 28
myCol = 28

# function to print a two lined rectangle
def twoLineRectangle():
    
    # Print the first star line, which consists of myRow number of stars
    for row in range(myRow):
        print("*", end = "")
    print()

    # Print the second star line, which also consists of myRow number of stars
    for row in range(myRow):
        print("*", end = "")
    print()

# end of twoLineRectangle()


# function to print a 3 star - 3 spaces pattern
def threeStarAccent():
    
    # Print the accent pattern, which is a series of stars and spaces
    # It consists of three lines, and the pattern is repeated on each line
    for row in range(3):
        # Print seven stars
        for column in range(7):
            print("*", end = "")
        # Print six spaces
        for column in range(6):
            print(" ", end = "")
        # Print two stars
        for column in range(2):
            print("*", end = "")
        # Print six spaces
        for column in range(6):
            print(" ", end = "")
        # Print seven stars
        for column in range(7):
            print("*", end = "")
        # Move to the next line
        print()
        
# end of threeStarAccent()



# function for a two line checker patttern
def checkers():
    
    # Print the penultimate pattern, which consists of two lines of alternating stars and spaces
    for row in range(5):
        # Print three stars
        for column in range(3):
            print("*", end = "")
        # Print three spaces
        for column in range(3):
            print(" ", end = "")
    # Move to the next line
    print()

    for row in range(4):
        # Print three spaces
        for column in range(3):
            print(" ", end = "")
        # Print three stars
        for column in range(3):
            print("*", end = "")
    # Move to the next line
    print()
    
# end of checkers()



#function to print a diamond with lines by its side
def diamond():
    
    # Print the diamond pattern
    diamondHeight = 7  # set the size of the diamond
    width = myCol - 4  # set the width of the output

    # Print the left half of the diamond
    for i in range(diamondHeight):
        # Print spaces to center the diamond
        for j in range(diamondHeight - i):
            print(" ", end="")
        # Print stars to form the left half of the diamond
        for j in range(2 * i + 1):
            print("*", end="")
        # Print spaces to separate the left and right halves of the diamond
        print(" " * ((width - 2 * diamondHeight) // 4), end="")
        # Print stars to form the right half of the diamond
        for j in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()

    # Print the right half of the diamond
    for i in range(diamondHeight - 2, -1, -1):
        # Print spaces to center the diamond
        for j in range(diamondHeight - i):
            print(" ", end="")
        # Print stars to form the left half of the diamond
        for j in range(2 * i + 1):
            print("*", end="")
        # Print spaces to separate the left and right halves of the diamond
        print(" " * ((width - 2 * diamondHeight) // 4), end="")
        # Print stars to form the right half of the diamond
        for j in range(2 * i + 1):
            print("*", end="")
        # Move to the next line
        print()
        
# end of diamond()



# function to print a two line pattern of 4,3,2,1 stars to 2,3,4 stars
def decreasingStarLinePattern():
    
    # Print the dotted pattern
    numStar = 4  # set the size of the pattern

    # loops for the number of stars 
    for colSection in range(numStar):
        # print a row of 4 asterisks
        for star in range(numStar):
            print("*", end="")
        # print some spaces
        print("   ", end="")
        # print a row of 3 asterisks
        for star in range(numStar-1):
            print("*", end="")
        # print some spaces
        print("   ", end="")
        # print a row of 2 asterisks
        for star in range(numStar-2):
            print("*", end="")
        # print some spaces
        print("  ", end="")
        # print a single asterisk
        print("*", end="")
        # print some spaces
        print("  ", end="")
        # print a row of 3 asterisks
        for star in range(numStar-2):
            print("*", end="")
        # print some spaces
        print("   ", end="")
        # print a row of 2 asterisks
        for star in range(numStar-1):
            print("*", end="")
        # print a newline
        print()
        
# end of decreasingStarLinePattern()
