from random import randint
import turtle

number=10
steps=200

pool = [turtle.Turtle(shape='circle') for i in range(number)]
a=[0]*number
b=[0]*number
i=0

for u in pool:
    u.penup()
    u.speed(100)
    u.goto(randint(-200, 200), randint(-200, 200))
    u.left(randint(-180,180))
    a[i]=randint(0,20)
    b[i]=randint(0,20)
    i=i+1

for i in range(steps):
    k=0
    for u in pool:
        if abs(a[k]+u.pos()[0])>=200:
           a[k]=-a[k]
        if abs((b[k]+u.pos()[1]))>=200:
           b[k]=-b[k] 
        u.goto(a[k]+u.pos()[0],b[k]+u.pos()[1] )
        k=k+1
               
        