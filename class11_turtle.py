'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ 2023
DESCRIPTION: 
DATE: 06/03/2023
'''

# this makes it so you don't need the module name to call the function
#from turtle import *

import turtle

# Example 1 ----------------------

def square():
    color("red")
    fd(100)

    # will turn left
    lt(90)

    color("green")
    fd(100)


    # will turn left
    lt(90)

    color("blue")
    fd(100)

    # will turn left
    lt(90)

    color("cyan")
    fd(100)

def mycircle():

    size = 3
    for shape in range(100):
        color("blue")
        circle(size+10)
        size += 3
        pu()
        fd(20)
        pd()
        fillcolor(randchoice())

# -------------------------------

def freeDanceTurtle():
   
   wn = turtle.Screen() # name and create a screen
   wn.bgcolor("lightgreen") # add background color to screen
   tess = turtle.Turtle() # create a turtle as an object
   tess.shape("turtle") # add turtle shape to pen
   tess.color("blue") 

   tess.penup()                # This is new
   size = 20
   
   for i in range(50):
      tess.stamp()             # Leave an impression on the canvas
      size = size + 3          # Increase the size on every iteration
      tess.forward(size)       # Move tess along
      tess.right(24)           #  ...  and turn her

   
   wn.mainloop()


def main():

    '''
    # Example 1 --------------
    for shape in range(4):
        square()

    mycircle()
    # ------------------------
    '''
    '''
    # Example 2 --------------
    freeDanceTurtle()
    '''
    
# main()

# Example 3 ----------------------
'''
distance  = .03
angle     = 89.5
increment =.03
segments  = 100 
right(90)  #   start in the center of a square view-space, facing "east"
viewSpace = 200   # set view space at 200

for i in range(segments):   
    forward ( distance * (.5 * viewSpace))   	# in the current direction
    right(angle)                        		# clockwise (to your right)
    distance += increment
ht()								# hide the turtle when done
done()							# close
'''
# -------------------------------



ninja = turtle.Turtle()

ninja.speed(10)

for i in range(180):
    ninja.forward(100)
    ninja.right(30)
    ninja.forward(20)
    ninja.left(60)
    ninja.forward(50)
    ninja.right(30)
    
    ninja.penup()
    ninja.setposition(0, 0)
    ninja.pendown()
    
    ninja.right(2)
    
turtle.done()

