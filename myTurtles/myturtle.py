"""This script shows you how to use the turtle module to draw squares."""
import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("red")

#create an instance of Turtle class and draw an yellow square
brad = turtle.Turtle()
brad.color("yellow")
brad.shape("turtle")
brad.forward(100)
brad.right(90)
brad.forward(100)
brad.right(90)
brad.forward(100)
brad.right(90)
brad.forward(100)

#create an instance of Turtle class and draw a blue square
geoff = turtle.Turtle()
geoff.color("blue")
geoff.shape("turtle")
geoff.forward(2)
geoff.forward(100)
geoff.right(90)
geoff.forward(100)
geoff.right(90)
geoff.forward(100)
geoff.right(90)
geoff.forward(100)


window.exitonclick()
