import pygame as p
import numpy as np
p.init()

FPS = 30
screen = p.display.set_mode((400, 600))
screen.fill((200, 200, 200))
#p.draw.rect(surface, (0, 0, 0), (0,0,0,0))
#p.draw.circle(screen, (0, 0, 0), (0, 0), 50)
#p.draw.line(screen, (0, 0, 0), (0,0), (0,0), 0)
#p.p.draw.polygon(screen, (255, 255, 0), [(100,100), (200,50), (300,100), (100,100)])
p.draw.aalines(screen, (0, 0, 0), False, [(0,0), (50,0), (70,30), (70,50)])
p.draw.polygon(screen, (0, 255, 255), [(0,200), (80,120), (120,150), (250,250), (300,80), (320,120), (400,30), (400,0), (0,0)])
p.draw.polygon(screen, (0, 255, 0), [(400,350),(200,370), (195,350),(100,350), (0,355), (0,600), (400,600)])
c=p.Surface((300,300),p.SRCALPHA)

def ell(x,y,m,n, surf):
    p.draw.ellipse(surf, (255, 255, 255), (x, y, m, n),0)
ell(0,125,150,50, c)
ell(0,155,20,40, c)
ell(0,191,20,40, c)
ell(100,155,20,40, c)
ell(100,191,20,40, c)
ell(120,165,20,40, c)
ell(120,201,20,40, c)
ell(20,165,20,40, c)
ell(20,201,20,40, c)
ell(100,227,30,10, c)
ell(120,237,30,10, c)
ell(0,227,30,10, c)
ell(20,237,30,10, c)
ell(110,45,40,110, c)
ell(110,20,50,30, c)
p.draw.ellipse(c, (255,0, 255), (125, 20, 15, 15),0)
p.draw.ellipse(c, (0,0, 0), (133, 23, 6, 6),0)
p.draw.polygon(c, (255, 255, 255), [(126,21), (126,6), (124,23)])
p.draw.polygon(c, (255, 255, 255), [(123,29), (103,14), (121,31)])

d=[0]*5
for i in range(5):
    if i==1:
        d[i]=c
    if i==0:
        d[i]=p.transform.smoothscale(c, (700,700))
    if i>1:
        d[i]=p.transform.smoothscale(c, (100,100))
    if (i==1) or (i==3):
        d[i]=p.transform.flip(d[i],True,False)

scr=p.Surface((150,150),p.SRCALPHA)
p.draw.ellipse(scr, (0, 155, 0), (0, 0, 150, 150))

a=p.Surface((60,30),p.SRCALPHA)
def g (x,y):
    p.draw.ellipse(a, (255, 255, 255), (x, y, 20, 10),0)
p.draw.ellipse(a, (255, 255, 0), (20, 8, 20, 10),0)
g(10,0)
g (30,0)
g(0,8)
g(40,8)
g(10,16)
g(30,16)

b=[0]*4
scr.blit(a,(40,95))
for i in range(4):
    b[i]=p.transform.rotate(a, 30+30*i)
scr.blit(b[0],(15,20))
scr.blit(b[3],(75,10))
scr.blit(b[2],(15,65))
scr.blit(b[1],(95,65))
screen.blit(scr,(150,450))

sc=[0]*4
for i in range(4):
    sc[i]=p.transform.smoothscale(scr,(int(150/(i+2)),int(150/(i+2))))
screen.blit(sc[0],(350,350))
screen.blit(sc[1],(50,360))
screen.blit(sc[2],(150,400))
screen.blit(sc[3],(370,520))

screen.blit(d[0],(-240,380))
screen.blit(d[1],(140,300))
screen.blit(d[2],(100,300))
screen.blit(d[3],(-10,290))
screen.blit(d[4],(180,350))

							   
p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in p.event.get():
		if event.type == p.QUIT:
			finished = True

p.quit()