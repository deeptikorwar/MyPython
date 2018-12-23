import turtle

window = turtle.Screen() #the canvas on which the turtle can draw
window.bgcolor("red")
tname="brad"
count=0
ang=0

#I am going to pass my turtle object to the function and execute the function
#many times

def mysquare(mypet, myang):
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
