# Unit 6 Turtle Problems

import turtle
window=turtle.Screen()

myturtle=turtle.Turtle()

myturtle.speed(0)
# Draw the coordinate system.
myturtle.goto(300,0)
myturtle.goto(-300,0)
myturtle.goto(0,0)
myturtle.goto(0,300)
myturtle.goto(0,-300)

#fancy function to lessen code
def RepeatingCode(color="black", x=0, y=0):
    myturtle.penup()
    myturtle.fillcolor(color)
    myturtle.goto(x,y)
    myturtle.pendown()
    myturtle.begin_fill()


def drawRectangle(color="black", x=0,y=0, width=30, height=30, direction=0):
    myturtle.color(color)
    RepeatingCode(color, x, y)
    # couldve put the sqaure in a for loop, but didnt
    myturtle.left(direction)
    myturtle.forward(width)
    myturtle.left(90)
    myturtle.forward(height)
    myturtle.left(90)
    myturtle.forward(width)
    myturtle.left(90)
    myturtle.forward(height)
    myturtle.end_fill()


def drawPolygon(color="black", x=0, y=0, length=30):
    myturtle.penup()
    myturtle.home() #this t.home gets in the way of using the repeating code function
    myturtle.color(color)
    myturtle.fillcolor(color)
    myturtle.goto(x,y)
    myturtle.pendown()
    myturtle.begin_fill()
    for i in range(5):
        myturtle.left(72)
        myturtle.forward(length)
    myturtle.end_fill()


def drawCircle(color="black",border_color="black", x=0, y=0, radius= 50):
    myturtle.hideturtle()
    myturtle.color(border_color)
    RepeatingCode(color, x, y)
    myturtle.circle(radius)
    myturtle.end_fill()

#drawing the circles
drawCircle(color="white",border_color="black", x=150, y=-300, radius=150) # this needs to be changed to
# only show an outline to be black
drawCircle(color="black", border_color="black", x=150, y=-275, radius=125)
drawCircle(color="blue", border_color="blue", x=150, y=-250, radius=100)
drawCircle(color="red", border_color="red", x=150, y=-225, radius=75)
drawCircle(color="yellow", border_color="yellow", x=150, y=-200, radius=50)

#drawing the squares
drawRectangle(color="red", x=10, y=5, width=300, height=300)
drawRectangle(color="green", x=10, y=153, width=212, height=212, direction=45)
drawRectangle(color="yellow", x=82, y=230, width=150, height=150, direction=45)
drawRectangle(color="blue", x=155, y=225, width=105, height=105, direction=45)
drawRectangle(color="orange", x=192, y=190, width=75, height=75, direction=45)

#drawing the hashtag rectangles:

#verticle ones(yellow and blue)
drawRectangle(color="yellow", x=-140, y=-70, width=25, height=210, direction=90)#
drawRectangle(color="blue", x=-230, y=-70, width=25, height=210, direction=90)#

#horizontal ones(red and green), have to do them in two parts so they go under and over the verticle ones correctly
drawRectangle(color="red", x=-310, y=-105, width=25, height=145, direction=180)
drawRectangle(color="red", x=-139, y=-105, width=25, height=40, direction=90)


drawRectangle(color="green", x=-310, y=-220, width=25, height=54, direction=90)
drawRectangle(color="green", x=-229, y=-220, width=25, height=130, direction=90)


#drawing the polygons

drawPolygon(color="red", x=-110, y=5, length =230)
drawPolygon(color="green", x=-145, y=35, length =170)
drawPolygon(color="yellow", x=-165, y=75, length =120)
drawPolygon(color="blue", x=-185, y=105, length =70)


window.exitonclick()
