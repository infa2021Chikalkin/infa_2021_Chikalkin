import turtle
import numpy as np
import random as r
turtle.speed(0)
for i in range(50):
	turtle.left(r.randint(-180,180))
	turtle.forward(r.randint(0, 50))