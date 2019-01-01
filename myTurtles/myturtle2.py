"""This script shows you how to use the turtle module to draw multiple squares,
 at various angles, using a function. The corners of the squares intersect to
  form a circle."""
import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("red")

tname="brad"
count=0 #counter to count the number of squares and create unique object names
ang=0 #variable to set the direction of the square

#I am going to pass my turtle object to the function and execute the function
# many times

def mysquare(mypet, myang):
    """Draws a square at the specified angle."""
    mypet = turtle.Turtle()
    mypet.color("yellow")
    mypet.shape("turtle")
    mypet.setheading(myang)
    for i in range(3):
        mypet.forward(100)
        mypet.right(90)
    mypet.forward(100)

#mysquare(tname)

while ang <= 360:
    count = count + 1
    app=str(count)
    tname = tname + app
    ang = ang + 10
    mysquare(tname,ang)

window.exitonclick()
