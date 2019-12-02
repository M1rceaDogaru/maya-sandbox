import random
from turtle import *
hideturtle()
shape("turtle")
speed(20)
colours = ["red", "orange", "yellow", "green", "LimeGreen", "cyan", "RoyalBlue1", "violet red", "gold"]
pensize(5) 
Screen().bgcolor("blue")
def vshape(size):
    right(25) 
    forward(size)
    backward(size)
    left(50)
    forward(size)
    backward(size)
    right(25)
def snowflakeArm(size):
    for x in range(0,4):
        forward(size)
        vshape(size)
    backward(size*4)
def snowflake(size):
    for x in range(0,18):
        color(random.choice(colours))
        snowflakeArm(size)
        right(20)
for i in range(0,10):
    size = random.randint(5,30)
    x = random.randint(-400,400)
    y = random.randint(-400,400)
    penup()
    goto(x,y)
    pendown()
    snowflake(size)

snowflake()
done()