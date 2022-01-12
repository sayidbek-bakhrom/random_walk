import turtle as turtle_module
import random

wn = turtle_module.Screen()
wn.setup(600, 600)
wn.tracer(0)


def create_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colors = (r, g, b)
    return colors


turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.hideturtle()
tim.penup()
tim.setheading(225)
tim.forward(340)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    wn.update()

    tim.dot(20, create_color())
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


wn.exitonclick()