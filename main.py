import turtle

mainTurtle = turtle.Turtle()
def denis(x,y):
    mainTurtle.penup()
    mainTurtle.goto(45,80)
    mainTurtle.pendown()
    mainTurtle.color("purple")

    mainTurtle.forward(100)
    mainTurtle.left(70)
    mainTurtle.forward(100)
    mainTurtle.left(110)
    mainTurtle.forward(100)
    mainTurtle.left(70)
    mainTurtle.forward(100)
mainTurtle.hideturtle()
turtle.exitonclick()