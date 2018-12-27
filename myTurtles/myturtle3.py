import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("black")

def mytriangle(ang):

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
