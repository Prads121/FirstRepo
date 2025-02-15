import turtle as t

t.bgcolor("black")
t.pensize(5)
t.speed(1)
t.color("red")
t.begin_fill()
t.fillcolor('red')
t.left(140)
t.forward(180)
t.circle(-90,180)
t.setheading(50)
t.circle(-90,180)
t.forward(180)
t.end_fill()
t.penup()
t.goto(100, 0) 
t.pendown()
msg= "Will you be my valentine"
t.write(msg, move=True,align ="left", font=("Arial", 24, "bold"))
t.hideturtle()
t.done()
print("what")

