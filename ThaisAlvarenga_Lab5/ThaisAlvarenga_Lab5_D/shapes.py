# Function for Pattern 1: rectangle
def rectangle():
    for rowsPattern1 in range(2):
        for numPatterLine in range(10):
            print("*", end="")
        print()
# end of rectangle()


        
# function for Pattern 2: two rectangles
def twoRectangles():
    for rowPattern2 in range(2):
        for colPattern in range (2):
            print(' ', end="")
            for numStars in range(3):
                print('*', end = "")
            print('', end="")
        print()
# end of twoRectangles()



# function for Pattern 3: triangle 
def triangle():
    #for each row
    for rows in range(1,4):
        print(' ', end = "")
        # print 3 stars
        for cols in range(rows):
            print("*", end="")
        print()
# end of triangle()



# Function for Pattern 4: inverted triangle
def invertedTriangle():
    # for all 3 rows of the triangle
    for i in range(1, 4):
            # print the spaces 
            for spaceNum in range(1,10-i):
                print(" ", end="")
            # print the starts 
            for starNum in range(i):
                print("*", end="")
            print()
# end of invertedTriangle()



# Function for space btw patterns
def doubleSpace():
    for spaceNum in range(2):
        # print space to next line
        print()
# end of doubleSpace
