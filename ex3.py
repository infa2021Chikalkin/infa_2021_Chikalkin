import turtle as t
import numpy as np
import random as r

def foo(an):
	t.penup()
	t.right((an)[0])
	t.forward((an)[1])
	t.pendown()
	t.right((an)[2])
	t.forward((an)[3])
	t.right((an)[4])
	t.forward((an)[5])
	t.right((an)[6])
	t.forward((an)[7])
	t.right((an)[8])
	t.forward((an)[9])
	t.right((an)[10])
	t.penup()
	t.forward((an)[11])
	t.right((an)[12])
	t.forward((an)[13])
	t.pendown()
inp = open('input.txt', 'r')
a=list(inp.readlines())
for i in range(4):
    a[i]=(a[i]).rstrip()
for i in range(4):
    a[i]=(a[i]).split(',')
for n in range(4):
	a[n]=list(map(float,a[n]))
[foo(a[1]),foo(a[2]),foo(a[1]),foo(a[3]),foo(a[0]), foo(a[0])]