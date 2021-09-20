import turtle
import numpy as np

turtle.shape('turtle')
turtle.speed(0)
turtle.penup()
turtle.backward(300)
turtle.pendown()
turtle.left(90)
for k in range (5):
	for i in range (1, 401):
		turtle.forward(0.5)
		turtle.right(0.45)
	for i in range (1, 401):
		turtle.forward(0.1)
		turtle.right(0.45)