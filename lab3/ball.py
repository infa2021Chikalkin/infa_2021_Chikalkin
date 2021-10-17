import pygame
from pygame.draw import *
from random import randint
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

def new_ball(d):
    '''рисует новый мячик '''
    circle(screen, d[3], (d[0], d[1]), d[2])
    
def move_ball(l):
    '''перемещает мячик'''
    l[0]=l[0]+l[4]
    l[1]=l[1]+l[5]
    circle(screen, l[3], (l[0], l[1]), l[2])
    return(l)

def click(event, k, s, m):
    '''удаляет мячик, в который попал игрок, и добавляет игроку очко''' 
    i = 1
    while i < m+1:
        if (((event.pos[0]-s[i][0])**2+(event.pos[1]-s[i][1])**2)<=((s[i][2])**2)):
            print("not bad!")
            k = k+1
            del s[i]
            m = m-1
        else:
            i=i+1
    return (k, s, m)
    
m = 0
w = 0

s=[0]*62 #создание списка, элементами которого будут мячи
for i in range(62):
    s[i]=[0]*6
    
a = list(range(-3, -1)) + list(range(1, 3))#задан диапазон значений скоростей мячей

pygame.display.update()
clock = pygame.time.Clock()
finished = False
k=0 

while (w <= FPS*30) and (not finished): #основной цикл программы
    clock.tick(FPS)
    
    if w % 15 == 0:#блок создания нового мяча
        s[m+1][0] = randint(100, 900)
        s[m+1][1] = randint(100, 500)
        s[m+1][2] = randint(10, 100)
        s[m+1][3] = COLORS[randint(0, 5)]
        if m != 0:
            new_ball(s[m])
        s[m+1][4] = a[randint(0, len(a)-1)]
        s[m+1][5] = a[randint(0, len(a)-1)]
        m = m+1
        
    for i in range(1, m+1):#блок реализации перемещения мячей
        s[i] = move_ball(s[i])
        if s[i][0] < 5 :#блок реализации случайного отражения мячей от стен
            s[i][4] = randint(1, 3)
            s[i][5] = a[randint(0, len(a)-1)]
        if s[i][0] > 995:
            s[i][4] = randint(-3, -1)
            s[i][5] = a[randint(0, len(a)-1)]
        if s[i][1] < 5 :
            s[i][5] = randint(1, 3)
            s[i][4] = a[randint(0, len(a)-1)]
        if s[i][1] > 595:
            s[i][5] = randint(-3, -1)
            s[i][4] = a[randint(0, len(a)-1)]
            
    
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if event.type == pygame.QUIT:#выхода из игры
            finished=True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:#нажатия на экран
            print('Click!')
            k, s, m = click(event, k, s, m)
            m = m
    w=w+1
    
    pygame.display.update()
    screen.fill(BLACK)
print('your result - ' , k , '/60')
pygame.quit()