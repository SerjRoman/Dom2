import turtle
mainTurtle = turtle.Turtle()

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