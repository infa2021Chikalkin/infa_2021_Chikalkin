import turtle

turtle.shape('turtle')
for i in range(1,11):
	turtle.forward(20*i)
	turtle.left(90)
	turtle.forward(20*i)
	turtle.left(90)
	turtle.forward(20*i)
	turtle.left(90)
	turtle.forward(20*i)
	turtle.penup()
	turtle.forward(10)
	turtle.left(90)
	turtle.backward(10)
	turtle.pendown()