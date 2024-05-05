# FILE: lab10.py
# J Hall, Transy U
# CS 1124, Fall 2020, Module 3
#
#           Construct a graphic window that displays a
#                  billboard with my name on it.
#

from graphics import *

def main():

    # parameters
    WIDTH = 400
    HEIGHT = 400

    ### Part 1: open sky blue window
    # open graphics window
    win = GraphWin("My Billboard: Lab 10", WIDTH, HEIGHT)

    # make background sky blue
    win.setBackground("light blue")

    # wait until mouse click to move on
    win.getMouse()

    ### Part 2: add a moon in upper left corner
    # set Point for moon center
    p = Point(WIDTH/8,HEIGHT/8)

    # set moon center and radius
    moon = Circle(p, 25)

    # set moon outline and fill color
    moon.setOutline("white")
    moon.setFill("white")

    # draw the moon
    moon.draw(win)

    # wait until mouse click to move on
    win.getMouse()

    ### Part 3: make the sign post
    # set Points for post
    p1 = Point(WIDTH/2, HEIGHT/2)
    p2 = Point(WIDTH/2, 400)

    # make the line
    post = Line(p1, p2)

    # set post outline and fill color
    post.setOutline("black")
    post.setFill("black")

    # set post thickness
    post.setWidth(10)

    # draw the post
    post.draw(win)

    # wait until the mouse click to move on
    win.getMouse()

    ### Part 4: make the billboard
    # set opposite rectangle points
    r1 = Point(WIDTH/4, HEIGHT-325)
    r2 = Point(WIDTH-100, HEIGHT/2-3)

    # make the rectangle
    board = Rectangle(r1, r2)

    # set billboard outline and fill color
    board.setOutline("violet")
    board.setFill("black")

    # set billboard outline thickness
    board.setWidth(5)

    # draw the post
    board.draw(win)

    # wait until the mouse click to move on
    win.getMouse()

    ### Part 5: display my name on the billboard
    # set text anchor point
    ap = Point(WIDTH/2, HEIGHT-264)

    # create text
    myName = Text(ap, "Jackson Hall")

    # set name color
    myName.setTextColor("magenta")

    # set name font
    myName.setFace("courier")

    # set name size
    myName.setSize(20)

    # set name style
    myName.setStyle("bold")

    # draw my name
    myName.draw(win)

    # wait until the mouse click to move on
    win.getMouse()

    ### Part 6: add a cloud
    # set opposite oval "points"
    o1 = Point(WIDTH-150, HEIGHT-150)
    o2 = Point(WIDTH-75, HEIGHT-100)

    # set the cloud puff centers
    puff1 = Point(WIDTH-142, HEIGHT-130)
    puff2 = Point(WIDTH-110, HEIGHT-150)
    puff3 = Point(WIDTH-82, HEIGHT-130)

    # set the sky rectangle points to flatten cloud bottom
    s1 = Point(WIDTH-150, HEIGHT-110)
    s2 = Point(WIDTH-75, HEIGHT-100)

    # make the cloud base
    cloudBase = Oval(o1, o2)

    # make the cloud puffs
    cloudPuff1 = Circle(puff1, 20)
    cloudPuff2 = Circle(puff2,20)
    cloudPuff3 = Circle(puff3,20)

    # make the sky rectangle
    extraSky = Rectangle(s1, s2)

    # set cloud base outline and fill color
    cloudBase.setOutline("white")
    cloudBase.setFill("white")

    # set cloud puffs outline and fill color
    cloudPuff1.setOutline("white")
    cloudPuff1.setFill("white")
    cloudPuff2.setOutline("white")
    cloudPuff2.setFill("white")
    cloudPuff3.setOutline("white")
    cloudPuff3.setFill("white")

    # set sky rectangle outline and fill color
    extraSky.setOutline("light blue")
    extraSky.setFill("light blue")

    # draw the cloud base
    cloudBase.draw(win)

    # draw the cloud puffs
    cloudPuff1.draw(win)
    cloudPuff2.draw(win)
    cloudPuff3.draw(win)

    # draw the sky rectangle
    extraSky.draw(win)

    # wait until the mouse click to move on
    win.getMouse()

    # close window
    win.close()
    
main()
