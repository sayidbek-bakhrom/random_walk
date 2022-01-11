import turtle as t
import random


window = t.Screen()
window.bgcolor("gray")

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


directions = [0, 90, 180, 270]


for __ in range(20):
  tim.color(random_color())
  tim.forward(35)
  tim.setheading(random.choice(directions))


window.exitonclick