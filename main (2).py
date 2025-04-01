import turtle
import random
from satellite import *

# Create a screen
screen = turtle.Screen()
screen.setup(400, 600)
screen.bgcolor("black")

turtle.speed(0)

# Write a function to draw star
def draw_star(x, y, size):
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    turtle.fillcolor("white")
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.forward(size)
    turtle.right(144)
    turtle.end_fill()

# Draw multiple stars using for loop
for i in range(20):
    x = random.randint(-200, 200)
    y =  random.randint(-100, 250)
    draw_star(x, y, 10)

# Call a function "draw_satellite(x,y)" to position satellite at random location
x = random.randint(-200, 200)
y =  random.randint(-100, 250)
draw_satellite(x, y)

# Write a function to draw crater
def draw_crater(x, y, size, color): 
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.dot(size, color)

# Create a moon of diameter 400
 
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

turtle.dot(400, "wheat")

# Call a draw_crater function to draw crater
draw_crater(80, -200, 40, "peru")
draw_crater(-80, -180, 80, "peru")
draw_crater(50, -150, 20, "peru")

# Move the turtle to display game title
turtle.penup()
turtle.goto(-130, 230)

# Set Color of game title
turtle.color("deepskyblue")

# Write "Game Title" and assign font
turtle.write("SPACE SHOOTER", font=("Arial", 24, "bold"))

turtle.hideturtle()