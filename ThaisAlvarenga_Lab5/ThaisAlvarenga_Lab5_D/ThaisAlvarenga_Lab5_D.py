'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates the following carpet pattern
DATE: 14/02/2023


**********
**********      

 ***  ***         
 ***  ***         


 *
 **
 ***              


 ***  ***
 ***  ***         

 
         *
        **
       ***        


 ***  ***
 ***  ***       


**********
**********
 

DATE:14/02/2023

'''


import shapes

def rug1():

    # print to title pattern
    print()
    print("Rug 1:")
    print()

    # print pattern using functions
    
    shapes.rectangle()

    shapes.doubleSpace()

    shapes.twoRectangles()

    shapes.doubleSpace()

    shapes.triangle()

    shapes.doubleSpace()

    shapes.twoRectangles()

    shapes.doubleSpace()

    shapes.invertedTriangle()

    shapes.doubleSpace()
    
    shapes.twoRectangles()

    shapes.doubleSpace()

    shapes.rectangle()
# end of rug 1


def rug2():
    # print to title pattern
    print()
    print("Rug 2:")
    print()

    shapes.triangle()
    
    shapes.rectangle()

    #keep drawing the two rectangles for 4 rows
    for row in range (4):
        shapes.twoRectangles()
    
    shapes.rectangle()

    shapes.invertedTriangle()

    shapes.rectangle()

    shapes.triangle()

    # draw the two rectangles for 2 rows
    for row in range (2):
        shapes.twoRectangles()

    # draw 1 rectangle for 2 rows
    for row in range (2):
        shapes.rectangle()

# end of rug 1
def main():

    # draw first rug pattern
    rug1()

    # draw second rug pattern
    rug2()
    

# end of main


main()
