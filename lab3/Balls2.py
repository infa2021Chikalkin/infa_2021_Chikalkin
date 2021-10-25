import pygame
import pygame.draw as p
import numpy as np
from random import randint

name = input('Введите свое имя')

pygame.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))

RED = (255, 0, 0)#блок задания цветовой гаммы мячей
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Special_Ball: #класс "особых" шаров, которые изменяют свой радиус
	def __init__(self, x, y, r0, r, color, dx, dy):
		'''задаем начальные параметры элемента класса'''
		self.x = x
		self.y = y
		self.r0 = r0
		self.r = r
		self.color = color
		self.dx = dx
		self.dy = dy
	def move_special_ball(self, screen, w): 
		'''реализует перемещение особых шаров'''
		self.x = self.x + self.dx
		self.y = self.y + self.dy
		self.r = int(self.r0*np.cos(np.pi/45*w))
		p.circle(screen, self.color, (self.x, self.y), self.r)
	def special_ball_collision (self, f, n): 
		'''реализует столкновения особых шаров между собой'''
		for i in range(n):
			if ((self != f[i]) and (self.x-f[i].x)**2 + (self.y-f[i].y)**2 <= (self.r + f[i].r)**2) and ((self.x-self.dx-f[i].x-f[i].dx)**2 + (self.y-self.dy-f[i].y-f[i].dy)**2) > (self.x-f[i].x)**2 + (self.y-f[i].y)**2:
				self.dx = -self.dx
				self.dy = -self.dy
	def special_wall_collision (self): 
		'''реализует столкновения особых шаров со стенами'''
		if (self.x < self.r) and (self.dx<0) :
			self.dx = randint(1, 3)
			self.dy = a[randint(0, len(a)-1)]
		if (self.x > 1000-self.r) and (self.dx>0) :
			self.dx = randint(-3, -1)
			self.dy = a[randint(0, len(a)-1)]
		if (self.y < self.r) and (self.dy < 0) :
			self.dy = randint(1, 3)
			self.dx = a[randint(0, len(a)-1)]
		if (self.y > 600-self.r) and (self.dy > 0):
			self.dy = randint(-3, -1)
			self.dx = a[randint(0, len(a)-1)]

class Ball: #класс обычных шаров
	def __init__(self, x, y, r, color, dx, dy):
		'''задаем начальные параметры элемента класса'''
		self.x = x
		self.y = y
		self.r = r
		self.color = color
		self.dx = dx
		self.dy = dy
		
	def move_ball(self, screen): 
		'''реализует перемещение шаров'''
		self.x = self.x + self.dx
		self.y = self.y + self.dy
		p.circle(screen, self.color, (self.x, self.y), self.r)
	def ball_collision (self, s, f, m, n): 
		'''реализует столкновения шаров между собой'''
		for i in range(m):
			if (self != s[i]) and ((self.x-s[i].x)**2 + (self.y-s[i].y)**2 <= (self.r + s[i].r)**2) and ((self.x-self.dx-s[i].x-s[i].dx)**2 + (self.y-self.dy-s[i].y-s[i].dy)**2) > (self.x-s[i].x)**2 + (self.y-s[i].y)**2:
				self.dx = -self.dx
				self.dy = -self.dy
		for i in range(n):
			if ((self.x-f[i].x)**2 + (self.y-f[i].y)**2 <= (self.r + f[i].r)**2) and ((self.x-self.dx-f[i].x-f[i].dx)**2 + (self.y-self.dy-f[i].y-f[i].dy)**2) > (self.x-f[i].x)**2 + (self.y-f[i].y)**2:
				self.dx = -self.dx
				self.dy = -self.dy
				
	def wall_collision (self): 
		'''реализует столкновения шаров со стенами'''
		if (self.x < self.r) and (self.dx<0) :
			self.dx = randint(1, 3)
			self.dy = a[randint(0, len(a)-1)]
		if (self.x > 1000-self.r) and (self.dx>0) :
			self.dx = randint(-3, -1)
			self.dy = a[randint(0, len(a)-1)]
		if (self.y < self.r) and (self.dy < 0) :
			self.dy = randint(1, 3)
			self.dx = a[randint(0, len(a)-1)]
		if (self.y > 600-self.r) and (self.dy > 0):
			self.dy = randint(-3, -1)
			self.dx = a[randint(0, len(a)-1)]
def click(s, f, event, k, m, n):
	'''удаляет мячик, в который попал игрок, и добавляет игроку очки''' 
	i = 0
	while i < m:
		if (((event.pos[0]-s[i].x)**2+(event.pos[1]-s[i].y)**2)<=((s[i].r)**2)):
			print("not bad!")
			k = k+1
			del s[i]
			m = m-1
		else:
			i=i+1
	i = 0
	while i < n:
		if (((event.pos[0]-f[i].x)**2+(event.pos[1]-f[i].y)**2)<=((f[i].r)**2)):
			print("not bad!")
			k = k + 3
			del f[i]
			n = n-1
		else:
			i=i+1
	return (k, s, f, m, n)
			
m = 0
w = 0
n=0

s=[0]*50 #создание списка, элементами которого будут мячи
	
f=[0]*20#создание списка, элементами которго будут особые мячи
	
a = list(range(-3, -1)) + list(range(1, 3))#задан диапазон значений скоростей мячей

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k=0 

while (w <= FPS*30) and (not finished): #основной цикл программы
	clock.tick(FPS)
	
	if (w % 15 == 0) and (m < 20):#блок создания нового мяча
		s[m] = Ball(randint(100, 900), randint(100, 500),  randint(10, 50),
		COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)])
		m = m+1
		
	if (w % 150 == 149) and (n < 5):#блок создания особого мяча
		f[n] = Special_Ball(randint(100, 900), randint(100, 500),  randint(30, 50), 0,
		COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)])
		n = n+1
		
	for i in range(m):#блок реализации перемещения мячей
		s[i].move_ball(screen)
		s[i].ball_collision(s, f, m, n)
		s[i].wall_collision()
	
	for i in range(n): #блок реализации перемещения особых мячей
		f[i].move_special_ball(screen, w)
		f[i].special_wall_collision()
		f[i].special_ball_collision(f, n)
		i = i+1
			
	for event in pygame.event.get():#блок обработки выполненных игроком действий
		if event.type == pygame.QUIT:#выхода из игры
			finished=True
			break
		elif event.type == pygame.MOUSEBUTTONDOWN:#нажатия на экран
			print('Click!')
			k, s, f, m, n = click(s, f, event, k, m, n)
	w=w+1
	
	pygame.display.update()
	screen.fill(BLACK)
	
print('your result - ' , k , 'points')#блок записи результатов в таблицу рекордов
p = open("table_of_records.txt", 'r')
t = p.readlines()
t[0] = t[0].rstrip()
h = [0]*6
names = [0]*6
for i in range (1, 6):
	t[i] = t[i].split()
	h[i - 1] = int(t[i][2])
	names[i - 1] = t[i][1]
i = 4
while (k > h[i]) and (i >= 0):
	h[i + 1] = h[i]
	h[i] = k
	names[i + 1] = names[i]
	names[i] = name
	i = i-1
for i in range(1, 6):
	t[i][2] = str(h[i - 1])
	t[i][1] = names[i - 1]
	t[i] = ' '.join(t[i])
t = '\n'.join(t)
p.close()	
q = open("table_of_records.txt", 'w')
q.write(t)
q.close()

pygame.quit()		
			
			
			
			
			
			
			
 
				
	