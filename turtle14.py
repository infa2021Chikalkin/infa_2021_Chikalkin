import turtle
import numpy as np

n=5
turtle.shape('turtle')
for i in range(n):
	turtle.forward(70)
	turtle.left(180-180/n)
turtle.penup()
turtle.left(90)
turtle.forward(200)
turtle.pendown()
n=11
for i in range(n):
	turtle.forward(70)
	turtle.left(180-180/n)
