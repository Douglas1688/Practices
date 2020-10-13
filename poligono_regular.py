import turtle as t
import random as r

def polygon(sides, length, x, y, color):
    t.penup()
    t.setposition(x,y)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for i in range(sides):
        t.forward(length)
        t.left(360//sides)
    t.end_fill()


t.hideturtle()
t.tracer(0)
for i in range(20):
    polygon(r.randrange(3,11), r.randrange(10,51),
            r.randrange(-250,251), r.randrange(-250,251),
            r.choice(("red","green","blue","black","yellow")))

t.update()
t.exitonclick()