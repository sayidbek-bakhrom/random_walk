import turtle as t
import random


window = t.Screen()
window.bgcolor("gray")
window.setup(300, 400)

tim = t.Turtle()
tim.pensize(10)
tim.speed(0)
t.colormode(255)


def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color

 
for __ in range(100):
  tim.color(random_color())
  tim.circle(100)
  tim.setheading(tim.heading() + 10)





window.exitonclick