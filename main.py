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
mainTurtle.hideturtle()

turtle.exitonclick()