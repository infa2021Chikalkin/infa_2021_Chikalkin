import math
from random import choice
import pygame
import pygame.draw as p
import numpy as np
from random import randint

name = input('Введите свое имя')

pygame.init()
pygame.font.init()

RED = (255, 0, 0)#блок задания цветовой гаммы мячей
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

FPS = 30
screen = pygame.display.set_mode((1000, 600))
screen.fill(WHITE)

class Ball: #класс обычных шаров
    def __init__(self, x, y, r0, r, color, dx, dy, j):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты элемента;
        ro - начальный радиус, r - текущий радиус;
        color - цвет, dx, dy - проекции скорости элеиента на оси;
        j - подтип элемента (1 - обычный мяч, 2 - мяч с изменяющимся радиусом, 3 - ядро)
        '''
        self.x = x
        self.y = y
        self.r0 = r0
        self.r = r0
        self.color = color
        self.dx = dx
        self.dy = dy
        self.j = j
        
    def move_ball(self, screen, w): 
        '''
        реализует перемещение шаров
        '''
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if self.j == 1:
            self.r = int(self.r0 * np.cos(np.pi/45 * w))
        if (self.j >= 2):
            self.dy = self.dy + 1
            self.j = self.j + 1
        p.circle(screen, self.color, (self.x, self.y), self.r)
    def ball_collision (self, s): 
        '''
        реализует столкновения шаров между собой
        '''
        for i in s:
            if i != 0:
                if (self != i) and ((self.x-i.x) ** 2 + (self.y-i.y) ** 2 <= (self.r + i.r) ** 2) and \
                ((self.x-self.dx-i.x-i.dx) ** 2 + (self.y-self.dy-i.y-i.dy) ** 2) > (self.x-i.x) ** 2 + (self.y-i.y) ** 2:
                    self.dx = - self.dx
                    self.dy = - self.dy
                 
    def wall_collision (self):    
        '''
        реализует столкновения шаров со стенами
        '''
        if (self.x < self.r) and (self.dx < 0) :
            self.dx = randint(1, 3)
            self.dy = a[randint(0, len(a)-1)]
        if (self.x > 1000 - self.r) and (self.dx > 0) :
            self.dx = randint(-3, -1)
            self.dy = a[randint(0, len(a)-1)]
        if (self.y < self.r + 35) and (self.dy < 0) :
            self.dy = randint(1, 3)
            self.dx = a[randint(0, len(a) - 1)]
        if (self.y > 600 - self.r) and (self.dy > 0):
            self.dy = randint(-3, -1)
            self.dx = a[randint(0, len(a) - 1)]
        
class Shell (Ball): #класс шара, которым стреляет пушка
    def __init__(self, x, y, r0, r, color, dx, dy, j):
        '''
        задаем начальные параметры элемента класса
        '''
        Ball.__init__(self, x, y, r0, r, color, dx, dy, j)
    def critical_collision (self, g, s, k):
        '''
        реализует столкновения шара-ядра с мишенью
        '''
        collision = False
        for i in range(len(s)):
            if s[i] != 0:
                if ((self.x - s[i].x) ** 2 + (self.y - s[i].y) ** 2 <= (self.r + s[i].r) ** 2):
                    collision = True
                    if s[i].j == 0:
                        k = k + 1
                    else:
                        k = k + 3
                    s[i] = 0
        if collision == True:
            g[v] = 0
        return (g, s, k)

    def critical_wall_collision (self):    
        '''
        реализует столкновения ядер со стенами
        '''
        if (self.x < self.r) and (self.dx < 0) or(self.x > 1000 - self.r) and (self.dx > 0) :
            self.dx = - self.dx // 2
        if (self.y < self.r + 35) and (self.dy < 0) or (self.y > 600 - self.r) and (self.dy > 0):
            self.dy = - self.dy // 2
            
def update(g, m):
        '''
        обновляет список уцелевших ядер
        '''
        i = m - 1
        while (i >= 0):
            if (g[i] == 0) or (g[i].j > 75):
                del(g[i])
                g.append(0)
                m = m - 1
            i = i - 1
        return (g, m)
        
def create_label(label, size, a, b, border, fill):
    '''
    создает надпись на заданной поверхности
    label - надпись
    size - размер шрифта
    a, b - размеры поверхности
    border - наличие рамки у пов-сти (логическая переменная)
    fill - заливка пов-сти (логическая переменная)
    '''
    f = pygame.font.SysFont(None, size)
    text = f.render(label, False, BLACK)
    surf = pygame.Surface((a, b), pygame.SRCALPHA)
    if border == True:
        pygame.draw.rect(surf, BLACK, (0, 0, a, b), 1)
    if fill == True:
        pygame.draw.rect(surf, GREEN, (0, 0, a, b), 0)
    surf.blit(text, (0, 0))
    return surf    
            
w = 0 #"счетчик времени"
k = 0 #число очков у игрока
l = 50 #начальная длина ствола пушки
m = 0 #кол-во летящих ядер
                        

s = [0] * 6 #создание списка, элементами которого будут мячи
g = [0] * 6 #создание списка, элементами которого будут ядра  
a = list(range(-3, -1)) + list(range(1, 3))#задан диапазон значений скоростей мячей

pygame.display.update()
clock = pygame.time.Clock()
finished = False #логическая переменная, отвечающая за закрытие программы
press = False #логическая переменная, проверяющая, зажата ли кнопка мыши в данный момент

label = 'Перезарядка орудия'
recharge = create_label(label, 50, 365, 40, True, False)#создана пов-сть с информацией о факте перезарядки орудия

Restart = create_label('Restart', 40, 100, 30, False, True) #создана пов-сть - кнопка рестарта
 
while (w <= FPS * 30) and (not finished): #основной цикл программы
    clock.tick(FPS)
    
    for i in range(5):
        if (s[i] == 0):#блок создания нового мяча
            s[i] = Ball(randint(100, 900), randint(100, 500),  randint(10, 50), 0,
            COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)], 0)
        
    if (w > 150) and (s[5] == 0):#блок создания особого мяча
        s[5] = Ball(randint(100, 900), randint(100, 500),  randint(30, 50), 0,
        COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)], 1)
        
    for i in s:#блок реализации перемещения мячей
        if i != 0:
            i.move_ball(screen, w)
            i.ball_collision(s)
            i.wall_collision()           
    
    r = pygame.mouse.get_pos() #кортеж из координат положения мыши
    x = r[0]
    y = 500 - r[1]
   
    sin_alpha = y / (x ** 2 + y ** 2) ** (1/2) #блок вычиления положения мыши относю пушки
    cos_alpha = x / (x ** 2 + y ** 2) ** (1/2)
        
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if event.type == pygame.QUIT:#выхода из игры
            finished = True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:#нажатие на кнопку мыши
            if (x >= 900) and (500 - y <= 30):
                k = 0
                w = 0
            else:
                press = True
        elif (event.type == pygame.MOUSEBUTTONUP) and (press == True):#отпускание кнопки мыши
            press = False
            if m < len(g): #ограничение на число ядер, одновременно находящихся на экране
                d = [0]*4
                d[0] = int((l * cos_alpha - 20 * sin_alpha + l * cos_alpha) / 2)
                d[1] = int(- (l * sin_alpha + 20 * cos_alpha + l * sin_alpha) / 2 + 500)
                d[2] = int(10 * l / 50 * cos_alpha)
                d[3] = int(- 10 * (l / 50) * sin_alpha)
                g[m] = Shell(d[0], d[1], 10, 10, BLACK, d[2], d[3], 2) #создание нового ядра
                m = m + 1
            l = 50
            
    if m >= len(s): #выводим на экран предупреждение - пушка перезаряжается и стрелять не может
        screen.blit(recharge, (300, 540))
    
    screen.blit(Restart, (900, 0)) #рисуем кнопку рестарта
    Current_result = create_label('Current result - ' + str(k), 40, 400, 30, False, False)
    #отображаем текущее кол-во очков у игрока на экране
    screen.blit(Current_result,(200, 0))
    
    if (press == True) and (l <= 300): #увеличение длины пушки
        l = l + 2 
    
    for v in range(m): #блок реализации перемещения ядер и их столкновений с мячами
        g[v].move_ball(screen, w)
        g, s, k = g[v].critical_collision(g, s, k)
    g, m = update(g, m)
    
    for i in range (m): #блок реализации столкновений ядер со стенами
        g[i].critical_wall_collision()
    g, m = update(g, m)
    
    pygame.draw.polygon(screen, BLACK, [[0, 500], [int(- 20 * sin_alpha), int(- 20 * cos_alpha + 500)], \
    [int(l * cos_alpha - 20 * sin_alpha), int(- l * sin_alpha - 20 * cos_alpha + 500)], \
    [int(l * cos_alpha), int(- l * sin_alpha + 500)]]) #рисуем пушку
    
    pygame.draw.line(screen, BLACK, (0, 30), (1000, 30), 5) #рисуем верхнюю грань обл. движения шаров
    
    w = w + 1
    
    pygame.display.update()
    screen.fill(WHITE)
    
print('your result - ' , k , 'points')#блок записи результатов в таблицу рекордов
p = open("table_of_records.txt", 'r')
t = p.readlines()
t[0] = t[0].rstrip()
h = [0] * 6
names = [0] * 6
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

pygame.display.update()
score = 'Your result = ' + str(k)

result = create_label(score, 50, 280, 40, False, False)
screen.blit(result, (320, 300))   
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if (event.type == pygame.QUIT) or (event.type == pygame.MOUSEBUTTONDOWN):#выхода из игры
            finished = True
    
pygame.quit()       
            
            
            
            
            
            
            
 
                
              
            
            
            
            
            
            
 
                
    