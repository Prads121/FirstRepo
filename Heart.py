import turtle as t

t.bgcolor("black")
t.pensize(5)
t.speed(3)
t.color("red")
t.begin_fill()
t.fillcolor('red')

t.left(140)
t.forward(180)
t.circle(-90, 180)
t.left(90)
t.circle(-90, 180)
t.forward(180)
t.setheading(50)
t.end_fill()

t.penup()
t.goto(200, 0)
t.pendown()

t.color("red")
t.write("Fuck You", font=("Arial", 24, "bold"), align="center")

t.hideturtle()
t.done()
