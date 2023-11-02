'''
NAME: Thais Alvarenga
COURSE: CADT-UH 1013EQ 2023
DESCRIPTION: Draws a generative art piece with Turtle graphics
DATE: 06/03/2023
'''

from turtle import *
from random import *

def main():

    # set color of border lines to white
    colormode(255)
    # set speed for draw
    speed('fastest')

    # set size to start from biggest circle to smallest
    size = 300

    # make circles of colors
    for shape in range(100):
        # set color to white
        color("white")
        # select random color to fill circle
        fillcolor((randint(0,255), randint(0,255), randint(0,255)))
        
        begin_fill()
        # draw circle
        circle(size+10)
        # reduce size
        size -= 3
        end_fill()
        # rotate circler around
        pu()
        lt(20)
        pd()

    # white circle lines to decorate (no fill)
    for shape in range(100):
        # set line color to white
        color("white")
        # draw circle
        circle(size+10)
        # increase size
        size += 3
        # rotate
        pu()
        lt(20)
        pd()
    
    done()

main()
