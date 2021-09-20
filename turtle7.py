import turtle
import numpy as np

turtle.shape('turtle')
for i in range(0,100):
	for k in range(0,40):
		turtle.forward((2*i)*np.sin(np.pi/200))
		turtle.left(1.8)
