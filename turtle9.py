import turtle
import numpy as np

turtle.shape('turtle')
def f(l, n):
	a=180*(n-2)/n
	turtle.right(a/2)
	for i in range(n):
		turtle.forward(l)
		turtle.left(180-a)
	turtle.left(a/2)
	turtle.penup()
	turtle.forward((l/2)/np.sin(np.pi/n)-((l+10)/2)/np.sin(np.pi/(n+1)))
	turtle.pendown()
for k in range (3,14):
	f(10+10*k,k)
	