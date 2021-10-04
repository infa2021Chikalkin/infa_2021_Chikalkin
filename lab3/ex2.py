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
p.draw.polygon(screen, (0, 255, 0), [(400,380),(200,370), (195,350),(100,350), (0,355), (0,600), (400,600)])
def ell(x,y,m,n):
    p.draw.ellipse(screen, (255, 255, 255), (x, y, m, n),0)
ell(50,400,150,50)
ell(50,430,20,40)
ell(50,466,20,40)
ell(150,430,20,40)
ell(150,466,20,40)
ell(170,440,20,40)
ell(170,476,20,40)
ell(70,440,20,40)
ell(70,476,20,40)
ell(150,502,30,10)
ell(170,512,30,10)
ell(50,502,30,10)
ell(70,512,30,10)
ell(160,320,40,110)
ell(160,295,50,30)
p.draw.ellipse(screen, (255,0, 255), (175, 300, 15, 15),0)
p.draw.ellipse(screen, (0,0, 0), (183, 303, 6, 6),0)
p.draw.polygon(screen, (255, 255, 255), [(176,301), (156,286), (174,303)])
p.draw.polygon(screen, (255, 255, 255), [(173,304), (153,289), (171,306)])
p.draw.ellipse(screen, (0, 155, 0), (250, 450, 150, 150))
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
screen.blit(a,(290,545))
b=[0]*4
for i in range(4):
    b[i]=p.transform.rotate(a, 30+30*i)
screen.blit(b[0],(265,470))
screen.blit(b[3],(325,460))
screen.blit(b[2],(265,515))
screen.blit(b[1],(345,510))
							   
p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in p.event.get():
		if event.type == p.QUIT:
			finished = True

p.quit()