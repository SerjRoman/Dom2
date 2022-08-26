import turtle
mainTurtle = turtle.Turtle()

def denis(x,y):
    mainTurtle.penup()
    mainTurtle.goto(x,y)
    mainTurtle.pendown()
    mainTurtle.fillcolor("blue")
    mainTurtle.begin_fill()
    mainTurtle.forward(100)
    mainTurtle.right(90)
    mainTurtle.forward(50)
    mainTurtle.right(90)
    mainTurtle.forward(100)
    mainTurtle.right(90)
    mainTurtle.forward(50)
    mainTurtle.end_fill()
denis(100,100)


def maxsim(x,y):
    mainTurtle.pencolor('orange')
    mainTurtle.penup()
    mainTurtle.goto(-100, -100)
    mainTurtle.pendown()
    mainTurtle.fillcolor('orange')
    mainTurtle.begin_fill
    mainTurtle.left(60)
    mainTurtle.forward(200)
    mainTurtle.right(120)
    mainTurtle.forward(200)
    mainTurtle.right(120)
    mainTurtle.forward(200)
    mainTurtle.end_fill


mainTurtle.hideturtle()

turtle.exitonclick()