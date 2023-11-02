'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates the following carpet pattern
DATE: 11/02/2023

****************************
****************************
*******      **      *******
*******      **      *******
*******      **      *******
***   ***   ***   ***   ***   
   ***   ***   ***   ***
       *  *
      ***  ***
     *****  *****
    *******  *******
   *********  *********
  ***********  ***********
 *************  *************
  ***********  ***********
   *********  *********
    *******  *******
     *****  *****
      ***  ***
       *  *
****   ***   **  *  ***   **
****   ***   **  *  ***   **
****   ***   **  *  ***   **
****   ***   **  *  ***   **
***   ***   ***   ***   ***   
   ***   ***   ***   ***
****************************
****************************

'''


# Set the number of rows and columns for the overall output
myRow = 28
myCol = 28

# Print the first star line, which consists of myRow number of stars
for row in range(myRow):
    print("*", end = "")
print()

# Print the second star line, which also consists of myRow number of stars
for row in range(myRow):
    print("*", end = "")
print()

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


# 3 star checker pattern from before
for row in range(5):
    for column in range(3):
        print("*", end = "")

    for column in range(3):
        print(" ", end = "")

print()

for row in range(4):
    for column in range(3):
        print(" ", end = "")

    for column in range(3):
        print("*", end = "")

print()


# Last 2 Rows of star lines (like from before)      
for row in range(28):
    print("*", end = "")

print()

for row in range(myRow):
    print("*", end = "")
    
print()
