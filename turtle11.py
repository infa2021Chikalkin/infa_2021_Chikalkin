import turtle
import numpy as np

turtle.shape('turtle')
for k in range (5):
	for i in range (1, 801):
		turtle.forward(0.5+k/20)
		turtle.left(0.45)
	for i in range (1, 801):
		turtle.forward(0.5+k/50)
		turtle.right(0.45)
		
	 