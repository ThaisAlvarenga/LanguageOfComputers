'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates the following carpet pattern
DATE: 09/02/2023


**********
**********         // Pattern 1


 ***  ***         
 ***  ***         // Pattern 2


 *
 **
 ***              // Pattern 3


 ***  ***
 ***  ***         // Pattern 4

 
         *
        **
       ***        // Pattern 5


 ***  ***
 ***  ***         // Pattern 6


**********
**********         // Pattern 7
 

DATE:08/02/2023

'''

# Pattern 1 (rectangle)
for rowsPattern1 in range(2):
    for numPatterLine in range(10):
        print("*", end="")
    print()
    
# Space 1
for spaceNum in range(2):
    # print space to next line
    print()

# Pattern 2 (3 stars)
for rowPattern2 in range(2):
    for colPattern in range (2):
        print(' ', end="")
        for numStars in range(3):
            print('*', end = "")
        print('', end="")
    print()

# Space 2
for spaceNum in range(2):
    # print space to next line
    print()

# Pattern 3 (rectangle)
for rows in range(1,4):
    print(' ', end = "")
    for cols in range(rows):
        print("*", end="")
    print()

# Space 3
for spaceNum in range(2):
    # print space to next line
    print()

# Pattern 4 (3 starts)
for rowPattern2 in range(2):
    for colPattern in range (2):
        print(' ', end="")
        for numStars in range(3):
            print('*', end = "")
        print('', end="")
    print()
    
# Space 4
for spaceNum in range(2):
    #print space to next line
    print()

# Pattern 5 (inverted triangle)

# for all 3 rows of the triangle
for i in range(1, 4):
        # print the spaces 
        for spaceNum in range(1,10-i):
            print(" ", end="")
        # print the starts 
        for starNum in range(i):
            print("*", end="")
        print()

# Space 5
for spaceNum in range(2):
    # print space to next line
    print()
    
# Pattern 6 (3 starts)
for rowPattern2 in range(2):
    # for the two lines of the pattern
    for colPattern in range (2):
        # print first space
        print(' ', end="")
        #print starts
        for numStars in range(3):
            print('*', end = "")
        # print second space
        print('', end="")
    # go to next line
    print()
    
# Space 6
for spaceNum in range(2):
    # print space to next line
    print()
    
# Pattern 7 (rectangle)
for rowsPattern1 in range(2):
    for numPatterLine in range(10):
        print("*", end="")
    print()

