# FILE: examGraphics.py
# J Hall, Transy U
# CS 1124, Fall 2020, Module 3
#
#           Use a graphics window to center a square with a border
#                              and a circle.
#

from graphics import *
def main():
     # parameters
    WIDTH = 400
    HEIGHT = 400

    # open graphics window
    win = GraphWin("Test 2, Question 2", WIDTH, HEIGHT)
    
    # wait until mouse click to move on
    win.getMouse()

    ### add a square with border in center
    # set Points for square's corners
    p1 = Point(WIDTH-250, HEIGHT-250)
    p2 = Point(WIDTH-150, HEIGHT-150)

    # create square
    square = Rectangle(p1, p2)

    # set square outline and fill color
    square.setOutline("orange")
    square.setFill("red")

    # set the border width
    square.setWidth(5)

    # draw the square
    square.draw(win)

    # wait until mouse click to move on
    win.getMouse()

    ### add a circle in the center
    # set point for cirlce center
    p3 = Point(WIDTH/2, HEIGHT/2)

    # set the circle's center
    c = Circle(p3, 50)

    # set the circle's outline and fill color
    c.setOutline("black")
    c.setFill("black")

    # draw the circle
    c.draw(win)

    # wait until mouse click
    win.getMouse()

    # close window
    win.close()


main()
