import turtle
T=turtle.Turtle()
T.hideturtle()
turtle.bgcolor("black")
cc=1
T.speed(100)
T.pencolor("white")
while cc<500:
    
    T.goto(250,0)
    T.forward(5+cc)
    T.right(91)
    T.penup()
    T.goto(0, 0)
    T.pendown()
    
    cc+=1


#letra J

T.pensize(10)
T.pencolor ("green")
T.goto(100, 0)
T.goto(100, -200)
T.goto(40,-270)
T.goto(10,-270)
T.goto(-30,-230)

#letra U
T.pensize(10)
T.pencolor("light green")
T.penup()
T.goto((250, 0))
T.pendown()
T.goto(250,-220)
T.goto(270,-270)
T.goto(340,-270)
T.goto(360,-220)
T.goto(360,0)

#letra A
T.pensize(10)
T.pencolor("yellow")
T.penup()
T.goto((450,0))
T.pendown()
T.goto(390,-270)
T.goto(450,0)
T.goto(510,-270)
T.penup()
T.goto(414.50,-160.30)
T.pendown()
T.goto(480.55,-160.30)

#letra N
T.pensize(10)
T.pencolor("orange")
T.penup()
T.goto(530,0)
T.pendown()
T.goto(530,-270)
T.penup()
T.goto(530,0)
T.pendown()
T.goto(600,-270)
T.goto(600,0)
