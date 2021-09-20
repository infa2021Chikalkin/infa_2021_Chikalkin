import turtle
import numpy as np

turtle.speed(0)
turtle.shape('turtle')
for k in range (3):
	for i in range (1, 801):
		turtle.forward(0.5)
		turtle.left(0.45)
	for i in range (1, 801):
		turtle.forward(0.5)
		turtle.right(0.45)
	turtle.left(60)
