"""This script shows you how to use the turtle module to draw multiple squares
using a function."""
import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("red")

#I am going to pass my turtle object to the function and execute the function
#multiple times

def mysquare(mypet, color):
    """Draws a square of the specified color."""
    mypet.color(color)
    mypet.shape("turtle")
    for i in range(3):
        mypet.forward(100)
        mypet.right(90)
    mypet.forward(100)

brad = turtle.Turtle()
mysquare(brad, "yellow")

geoff = turtle.Turtle()
#Let's move geoff by two spaces so that he does not overwrite brad
geoff.forward(2)
mysquare(geoff,"blue")

window.exitonclick()
