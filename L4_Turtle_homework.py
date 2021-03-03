import turtle
import math
canvas=turtle.Screen()
canvas.title('Triforce')
def draw_spiral(t, n, length=5, a=0.1, b=0.0007):
    theta = 0.0

    for i in range(n):
        t.fd(length)
        dtheta = 1 / (a + b * theta)

        t.lt(dtheta)
        theta += dtheta

def make_turtle(color, size, shape):
    t = turtle.Turtle()
    t.color(color)
    t.pensize(size)
    t.shape(shape)
    t.speed(0)
    t.penup()
    True
    return t    
a = 0
a = int (a)
for x in [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 310]:
    turtle.tracer(1000,0)
    bob = make_turtle("black",1, "turtle")
    a = a+ 5
    draw_spiral(bob, n = a + a)

turtle.mainloop()
turtle.done()

try:
    turtle.bye()   
except turtle.Terminator:
    pass