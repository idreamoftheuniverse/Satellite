import turtle
import random

screen = turtle.Screen()

screen.register_shape("s_satellite.png")
screen.register_shape("m_sat.png")
screen.register_shape("big_sat.png")

def draw_satellite(x,y):
    sat = turtle.Turtle()
    angle = random.randint(-90, 90)
    sat.penup()
    sat.left(angle)
    img = random.randint(1, 3)
    if img == 1:
        sat.goto(x, y)
        sat.shape("s_satellite.png")
    if img == 2:
        sat.goto(x, y)
        sat.shape("m_sat.png")
    else:
        sat.goto(x, y)
        sat.shape("big_sat.png")
        
def write_msg(x, y, msg, size,color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.color(color)
    turtle.write(msg, font=("Arial", size, "bold"))
    turtle.hideturtle()
        
turtle.hideturtle()