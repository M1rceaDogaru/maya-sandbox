import random
from turtle import *
shape("turtle")
speed(5)
colours = ["blue", "purple", "cyan", "plum", "LimeGreen", "yellow", "orange", "red", "HotPink"]
pensize(5) 
Screen().bgcolor("lemon chiffon")
def vshape():
    right(25) 
    forward(50)
    backward(50)
    left(50)
    forward(50)
    backward(50)
    right(25)
def snowflakeArm():
    for x in range(0,4):
        forward(30)
        vshape()
    backward(120)
def snowflake():
    for x in range(0,18):
        color(random.choice(colours))
        snowflakeArm()
        right(20)

snowflake()
done()