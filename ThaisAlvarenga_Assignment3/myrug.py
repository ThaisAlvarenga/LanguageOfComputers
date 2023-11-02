'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ Language of Computers
DESCRIPTION: Generates the following carpet pattern using functions from a module
DATE: 19/02/2023

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
# import module with shapes for the carpet
import shapesCarpet

def main():
    # you can reassign the varibles of the module to the value you want
    shapesCarpet.myRow  = 28
    shapesCarpet.myCol  = 28

    # print rectangle shape
    shapesCarpet.twoLineRectangle()

    # print 3 star pattern
    shapesCarpet.threeStarAccent()

    # print checker pattern
    shapesCarpet.checkers()

    # print diamond
    shapesCarpet.diamond()

    # print the star line pattern
    shapesCarpet.decreasingStarLinePattern()

    # print checkers again
    shapesCarpet.checkers()

    # print rectangle again
    shapesCarpet.twoLineRectangle()

#end of main function

main()
