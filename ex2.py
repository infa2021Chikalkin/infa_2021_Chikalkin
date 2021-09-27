import turtle as t
import numpy as np
import random as r

def foo(an):
    t.penup()
    t.right(an[0])
    t.forward(an[1])
    t.pendown()
    t.right(an[2])
    t.forward(an[3])
    t.right(an[4])
    t.forward(an[5])
    t.right(an[6])
    t.forward(an[7])
    t.right(an[8])
    t.forward(an[9])
    t.right(an[10])
    t.penup()
    t.forward(an[11])
    t.right(an[12])
    t.forward(an[13])
    t.pendown()
a0=(0,0,0,20,90, 40,90,20,90,40,90,20,0,20)
a1=(90,20,-135,20*np.sqrt(2),135,40,180, 0,0,0,0,40,90,20)
a4=(0,0,90,20,-90,20,-90,20,180,40,180,40,90,20)
a7=(0,0,0,20,135,20*np.sqrt(2),-45,20,180,0,0,40,90,40)
[foo(a1),foo(a4),foo(a1),foo(a7),foo(a0), foo(a0)]
