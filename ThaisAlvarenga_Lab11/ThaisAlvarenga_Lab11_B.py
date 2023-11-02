'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ 2023
DESCRIPTION: Draws a generative art piece with Turtle graphics, using functions
and two objects
DATE: 06/03/2023
'''


from turtle import *
import random

# function to draw a square
def drawSquare(turtle, size):
    # for each side of square
    for side in range(4):
        # make turtle move forward by the size of square side
        turtle.forward(size)
        # rotate 90 degrees
        turtle.right(90)
# end


# define a function to change the color of the turtles to a random color
def changeColor(first,second):
    thais.color(random.choice(['red', 'green', 'blue', 'orange', 'purple']))
    mohammad.color(random.choice(['red', 'green', 'blue', 'orange', 'purple']))
# end change_colo


def setupTurtleObjects():
    # set shape of the obejcts to a turtle
    thais.shape("turtle")
    mohammad.shape("turtle")

    # make the speed to draw fast
    thais.speed(50)
    mohammad.speed(50)

    # set turtle objects to starting positions

    # set thais -100 
    thais.penup()
    thais.goto(-100, 0)
    thais.pendown()

    # make mohammad 100 
    mohammad.penup()
    mohammad.goto(100, 0)
    mohammad.pendown()

    # set colors of each object
    thais.color("green")
    mohammad.color("cyan")
    
# end


# declare turtle objects as global variables
thais = Turtle()
mohammad = Turtle()


def main():

    # set up turtle objects 
    setupTurtleObjects()
    
    # for the number of squares you will make
    for squareNum in range(19):
        # draw quare for first object
        drawSquare(thais, 100)
        # draw quare for second object
        drawSquare(mohammad, 100)
        
        # rotate 
        thais.right(10)
        # rotate in opposite direction to first object
        mohammad.left(10)

    # tell user to click
    thais.write("Click on screen to change turtle color", font=("Arial", 30, "normal"))

    # change color of tutle objects
    onscreenclick(changeColor)

    done()
    
#end of main  

main()




'''
'''
