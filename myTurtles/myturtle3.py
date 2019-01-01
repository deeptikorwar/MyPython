"""This script shows you how to use the turtle module to draw multiple
 trianlges, at various angles, using a function. The corners of the trianlges
  intersect to form a circle."""
import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("black")

def mytriangle(ang):
    """Draws a triangle at the specified angle."""
    mypet = turtle.Turtle()
    mypet.setheading(ang)
    mypet.color("white")
    mypet.shape("turtle")
    mypet.forward(100)
    mypet.left(120)
    mypet.forward(100)
    mypet.left(120)
    mypet.forward(100)

x = 0
while x <= 360:
    mytriangle(x)
    x = x + 10

window.exitonclick()

