import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("red")

#I am going to pass my turtle object to the function and execute the function
#many times

def mysquare(mypet):
    mypet.color("yellow")
    mypet.shape("turtle")
    for i in range(3):
        mypet.forward(100)
        mypet.right(90)
    mypet.forward(100)

brad = turtle.Turtle()
mysquare(brad)

geoff = turtle.Turtle()
geoff.color("blue")
geoff.forward(2)
mysquare(geoff)
#how do I make geoff blue? It is overwritten by yellow in mysquare... how do
# I avoid that???

window.exitonclick()
