import turtle as t
import numpy as np
import random as r
t.shape('circle')
x=0
y=0
t.speed(0)
t.penup()
t.goto(-300,0)
t.pendown()
def foo(Vx, Vy,a):
    s=Vy
    while (0==0):
        t.goto (Vx*0.1+t.pos()[0], Vy*0.1+t.pos()[1])
        if t.pos()[1]<0:
            t.goto (t.pos()[0],0)
            break
        Vy = Vy+a*0.1
Vx=[0]*10
Vy=[0]*10
a=-0.5
for i in range(10):
    Vx[i]=3-0.3*i
    Vy[i]=10-1*i
for i in range(10):
    foo(Vx[i], Vy[i], a)