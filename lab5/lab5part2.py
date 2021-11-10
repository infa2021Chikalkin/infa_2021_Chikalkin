import math
from random import choice
import pygame
import pygame.draw as p
import numpy as np
from random import randint

RED = (255, 0, 0)#блок задания цветовой гаммы мячей
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

class Ball: #класс обычных шаров
    def __init__(self, x: int, y: int, r0: int, r: int, color: tuple, dx: int, dy: int, j: int, t: int):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты элемента;
        ro - начальный радиус, r - текущий радиус;
        color - цвет, dx, dy - проекции скорости элеиента на оси;
        j - подтип элемента (0 - обычный мяч, 1 - мяч с изменяющимся радиусом, 2 - ядро, 
        3 - картечь, 4 - осколки картечи)
        '''
        self.x = x
        self.y = y
        self.r0 = r0
        self.r = r0
        self.color = color
        self.dx = dx
        self.dy = dy
        self.j = j
        self.t = t
        
    def move_ball(self, screen: pygame.Surface, w: int ): 
        '''
        реализует перемещение шаров
        '''
        self.x = self.x + self.dx
        self.y = self.y + self.dy
        if self.j == 1:
            self.r = int(self.r0 * np.cos(np.pi/45 * w))
        if (self.j >= 2) and (self.j <= 4):
            self.dy = self.dy + 1
            self.t = self.t + 1
        if (self.j != 5) or (w % 6 >= 3):
            p.circle(screen, self.color, (self.x, self.y), self.r)
    def ball_collision (self, s: list): 
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

class Border_Points:
    '''
    класс граничных точек танка, служащий для установления факта столкновения обЪекта с танком  
    '''
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
class Shell (Ball): #класc cнарядов, которым стреляет пушка танка
    def __init__(self, x: int, y: int, r0: int, r: int, color: tuple, dx: int, dy: int, j: int, t: int):
        '''
        задаем начальные параметры элемента класса
        '''
        Ball.__init__(self, x, y, r0, r, color, dx, dy, j, t)
    def critical_collision (self, g: list, s: list, k: int, v: int):
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
            if self.j != 3:
                g[v] = 0
            else:
                g[v] = explosion_of_buckshot(self) #взрыв картечи
        return (g, s, k)

    def critical_wall_collision (self):    
        '''
        реализует столкновения ядер со стенами
        '''
        if (self.x < self.r) and (self.dx < 0) or(self.x > 1000 - self.r) and (self.dx > 0) :
            self.dx = - self.dx // 2
        if (self.y < self.r + 35) and (self.dy < 0) or (self.y > 600 - self.r) and (self.dy > 0):
            self.dy = - self.dy // 2
            
class Buckshot (Shell): #класс снарядов картечного типа
    def __init__(self, x: int, y: int, r: int, color: tuple, dx: int, dy: int, children: list, j: int, t: int, explosion: bool):
        '''
        задаем начальные параметры элемента класса:
        x, y - координаты элемента;
        r - радиус;
        color - цвет, dx, dy - проекции скорости элемента на оси;
        children - список, в котором будут храниться дочерние снаряды - осколки картечи),
        t - время полета снаряда)
        '''
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.dx = dx
        self.dy = dy
        self.children = children
        self.j = j
        self.t = t
        self.explosion = explosion
        
def collision_buckshot_with_other_shells(T: list, k: int):
    '''
    реализует столкновения картечного снаряда с ядрами
    '''
    for h in range(2):
        for i in range((T[k].m)):
            if ((T[h].shells[i].x - T[k].buckshot.x) ** 2 + (T[h].shells[i].y - \
            T[k].buckshot.y) ** 2 <= (T[h].shells[i].r + T[k].buckshot.r) ** 2):
                T[k].buckshot = explosion_of_buckshot(T[k].buckshot)
                T[h].shells[i] = 0
    return T

class Bombs (Ball):
    def __init__(self, x: int, y: int, r0: int, r: int, color: tuple, dx: int, dy: int, j: int, t: int):
        '''
        задаем начальные параметры элемента класса
        '''
        Ball.__init__(self, x, y, r0, r, color, dx, dy, j, t)
    def collision_bombs_with_tanks(self, location, number, lives):
        '''
        реализует попадание бомб в танки
        '''
        x = location - (-1) ** number * 15
        if (self.x - x) ** 2 + (self.y - 600) ** 2 <= (self.r ** 2 + 45 ** 2):
            self.r = 0
            lives = lives - 1
        return lives

class Tank:
    def __init__(self, location: int, dx: int, l: int, color: tuple, lives: int, press: list, alpha: float, shells: list, \
    buckshot: Buckshot, shooting_with_buckshot: bool,  m: int, border: list, number: int):
        '''
        задаем начальные параметры элемента класса:
        location - положение танка;
        dx - скорость перемещения танка
        l текущая длина пушка танка;
        color - цвет;
        lives - число оставшихся у танка жизней
        press - список логических переменных, описывающих характер движения танка
        alpha - угол наклона пушки в данный момент времени
        shells - список активных ядер, выпущенных танком
        buckshot - картечный снаряд танка
        shooting_with_buckshot - логическая переменная, устанавливающая тип снаряда
        m - число активных ядер танка
        border - граничные точки танка (нужны для установления факта попадания в танк
        number - номер танка
        '''
        self.location = location
        self.dx = dx
        self.l = l
        self.color = color
        self.lives = lives
        self.press = press
        self.alpha = alpha
        self.shells = shells
        self.buckshot = buckshot
        self.shooting_with_buckshot = shooting_with_buckshot
        self.m = m 
        self.border = border
        self.number = number
    
    def move_tank (self, screen: pygame.Surface, w: int):
        '''
        реализует перемещение танка
        '''
        if self.number == 2: #перемещение танка игрока
            if (self.press[1] == True) and (self.location > 60):
                self.location = self.location - 3
            if (self.press[2] == True) and (self.location < 420):
                self.location = self.location + 3     
        else:
            if (self.location < 580) or (self.location > 940): #перемещение танка противника
                self.dx = - self.dx
            self.location = self.location + self.dx
        if (self.press[0] == True) and (self.l <= 120): #увеличение длины пушки
            self.l = self.l + 2 
        if (self.press[3] == True) and (self.alpha < np.pi / 3): #изменение угла наклона пушки
            self.alpha = self.alpha + np.pi / 180 
        if (self.press[4] == True) and (self.alpha > 0):
            self.alpha = self.alpha - np.pi / 180 
         
        self.border[0] = Border_Points(self.location - (-1) ** self.number * 60, 560) #граничные точки танка
        self.border[1] = Border_Points(self.location - (-1) ** self.number * 30, 600)
        self.border[2] = Border_Points(self.location, 600)
        self.border[3] = Border_Points(self.location + (-1) ** self.number * 30, 560)
        self.border[4] = Border_Points(self.location, 560)
        self.border[5] = Border_Points(self.location, 530)
        self.border[6] = Border_Points(self.location - (-1) ** self.number * 30, 530)
        self.border[7] = Border_Points(self.location - (-1) ** self.number * 30, 560)
        for i in range(8):
            self.border[i + 8] = Border_Points((self.border[i].x + self.border[(i + 1) % 8].x) // 2, (self.border[i].y + self.border[i + 1].y) // 2)
            
        pygame.draw.polygon(screen, self.color, [[self.location, 560], \
        [self.location + (-1) ** self.number * int(- 20 * np.sin(self.alpha)), int(- 20 * np.cos(self.alpha) + 560)], \
        [self.location + (-1) ** self.number * int(self.l * np.cos(self.alpha) - 20 * np.sin(self.alpha)), int(- self.l * np.sin(self.alpha) - 20 * np.cos(self.alpha) + 560)], \
        [self.location + (-1) ** self.number * int(self.l * np.cos(self.alpha)), int(- self.l * np.sin(self.alpha) + 560)]]) #рисуем пушку
        pygame.draw.polygon(screen, GREEN, [[self.location - (-1) ** self.number * 60, 560], [self.location - (-1) ** self.number * 30, 600],\
        [self.location, 600], [self.location + (-1) ** self.number * 30, 560], [self.location, 560], [self.location, 530],\
        [self.location - (-1) ** self.number * 30, 530], [self.location - (-1) ** self.number * 30, 560]])#рисуем корпус танка
          
def updates (shells, m):
        '''
        обновляет список уцелевших ядер
        '''
        i = m - 1
        while (i >= 0):
            if (shells[i] == 0) or (shells[i].t > 75):
                del(shells[i])
                shells.append(0)
                m = m - 1
            i = i - 1
        return (shells, m)
        
def update_bombs(bombs: list):
    '''
    обновляет список бомб
    '''
    i = len(bombs) - 1
    while (i >= 0):
        if bombs[i].r == 0:
            del(bombs[i])
        i = i - 1
    return (bombs)
        
def create_label(label, size: int, a: int, b: int, border: bool, fill: bool):
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

def starting_parametres(location: int, l: int, alpha: float, number: int):
        '''
        вспомогательная функция, устанавливающая начальные параметры любого снаряда
        '''
        d = [0]*4
        d[0] = int(location + (-1) ** number * l * np.cos(alpha))
        d[1] = int(- l * np.sin(alpha) - 10 * np.cos(alpha) + 560)
        d[2] = int(10 * l / 50 * np.cos(alpha) * (-1) ** number)
        d[3] = int(- 10 * (l / 50) * np.sin(alpha))
        return d

def create_shell(shells, location: int, m: int, l: int, alpha: float, number: int):
    '''
    создаем ядро, которым стреляет танк в данный момент
    '''
    if m < len(shells): #ограничение на число ядер, одновременно находящихся на экране
        d = starting_parametres (location, l, alpha, number)
        shells[m] = Shell(d[0], d[1], 10, 10, BLACK, d[2], d[3], 2, 0) #создание нового ядра
        m = m + 1
    return shells, m
    
def create_buckshot (buckshot: Buckshot, location: int, l: int, alpha: float, number: int):
    '''
    создаем картечный снаряд, которым стреляет танк в данный момент
    '''
    d = starting_parametres (location, l, alpha, number)
    buckshot = Buckshot(d[0], d[1], 10, GRAY, d[2], d[3], [0]*7, 3, 0, False) #создание нового ядра
    return buckshot

def collision_buckshot_with_wall(buckshot: Buckshot):
    '''
    реализуем столкновение картечного снаряда со стенами, в результате
    которого происходит разрыв снаряда
    '''
    if (buckshot.x < buckshot.r) and (buckshot.dx < 0) or(buckshot.x > 1000 - buckshot.r) and (buckshot.dx > 0)\
    (buckshot.y < buckshot.r + 35) and (buckshot.dy < 0) or (buckshot.y > 600 - buckshot.r) and (buckshot.dy > 0):
        buckshot = explosion_of_buckshot(buckshot)
    return buckshot
def shout (Tank: Tank):
    '''
    реализует выстрел танка
    '''
    if Tank.shooting_with_buckshot == False:
        Tank.shells, Tank.m = create_shell(Tank.shells, Tank.location, Tank.m, Tank.l, Tank.alpha, Tank.number)
    else:
        if Tank.buckshot == 0:
            Tank.buckshot = create_buckshot (Tank.buckshot, Tank.location, Tank.l, Tank.alpha, Tank.number)
    return Tank
      
def shell_collisions (T: list):
    '''
    реализует столкновения ядер между собой
    '''
    for i in range(T[0].m):
        for k in range (T[1].m):
            if T[1].shells[k] !=  0:
                if ((T[0].shells[i].x - T[1].shells[k].x) ** 2 + (T[0].shells[i].y - \
                T[1].shells[k].y) ** 2 <= (T[0].shells[i].r + T[1].shells[k].r) ** 2):
                    T[0].shells[i] = 0
                    T[1].shells[k] = 0
                    break
    return T

def explosion_of_buckshot(buckshot: Buckshot):
    '''
    реализует взрыв картечного снаряда
    '''
    for i in range(7):
        buckshot.children[i] = Shell(buckshot.x, buckshot.y, 4, 4, GRAY, randint(buckshot.dx - 10, buckshot.dx + 10),\
        randint(buckshot.dy - 10, buckshot.dy + 10), 4, buckshot.t)
    buckshot.explosion = True
    return buckshot 

def collision_with_barrier(object):
    '''
    реализует столкновения с барьером в центре игрового поля
    '''
    if (object != 0) and ((object.x - 500) ** 2 + (object.y - 600) ** 2 < 60 ** 2) and \
    ((object.x + object.dx - 500) ** 2 + (object.y + object.dy - 600) ** 2 < (object.x - 500) ** 2 + (object.y - 600) ** 2):
        object.dx = - object.dx
        object.dy = - object.dy
        if object.j == 3:
            object = explosion_of_buckshot(object)
    return object
def hit(points: list, shell: Shell, lives: int, stage: int):
    '''
    Реализует случай попадания снаряда в танк. Если это первый этап игры (stage = 1) либо скорость ядра невелика, оно 
    просто отскакивает от танка, иначе танк поврежден, ядро (shell) исчезает с экрана. 
    Point - список граничных точек танка
    '''
    for i in points:
        if (shell.x - i.x) ** 2 + (shell.y - i.y) ** 2 <= (shell.r ** 2):
            if (shell.dx ** 2 + shell.dy ** 2) >= 20 and (stage == 2):
                shell = 0
                lives = lives - 1
            else:
                shell.dx = - shell.dx // 2
                shell.dy = - shell.dy // 2
            break
    return shell, lives
            
w = 0 #"счетчик времени"
s = [0] * 6 #создание списка, элементами которого будут мячи
bombs = [] #создание списка, элементами которого будут бомбы
a = list(range(-3, -1)) + list(range(1, 3))#задан диапазон значений скоростей мячей

border = [0] * 16 #списки граничных точек    
border1 = [0] * 16  
T34 = Tank(60, 0, 40, GREEN, 3, [False] * 5, 0, [0] * 4, 0, False, 0, border, 2) #создаем наш танк
Tiger = Tank(940, - 2, 40, GREEN, 3, [False] * 5, 0, [0] * 4, 0, False, 0, border1, 1) #создаем танк противника (Тигр)
T = [0, 0] #создан список из элементов класса Tank
T[0] = T34
T[1] = Tiger
pygame.init()
pygame.font.init()

FPS = 30
screen = pygame.display.set_mode((1000, 600))
screen.fill(WHITE)

pygame.display.update()
clock = pygame.time.Clock()
finished = False #логическая переменная, отвечающая за закрытие программы

label = 'Перезарядка'
recharge = create_label(label, 40, 200, 30, True, False)#создана пов-сть с информацией о факте перезарядки орудия

Restart = create_label('Restart', 40, 100, 30, False, True) #создана пов-сть - кнопка рестарта

text = [0]*9 #инструкция для игрока
table  = [0]*9
text[0] = 'На первом этапе игры Вам необходимо сбить'
text[1] = 'как можно больше шаров - это даст очки жизни Вашему танку.' 
text[2] = 'Снаряды учебные - вражескому танку вреда они не наносят.'
text[3] = 'Чтобы сбивать больше снарядов, используйте картечь'
text[4] = '(переключение типа снаряда осуществляется клавишой Shift)' 
text[5] = 'На втором этапе игры (когда шары исчезнут)'
text[6] = 'Вам предстоит дуэль с вражеским танком.'
text[7] = '(Да, картечь против него не поможет, поэтому эта функция отключена).' 
text[8] = '                     Удачи!' 
for i in range(9):
    table[i] = create_label(text[i], 40, 1000, 60, False, False)
    
screen.fill(WHITE)
w = 0
for i in range(9):
    screen.blit(table[i], (5, 30 + 60 * i))
pygame.display.update()

while (w <= FPS * 4) and (not finished): #игрок читает инструкцию к игре
    clock.tick(FPS)
    w = w + 1
 
pygame.display.update()
while (w <= FPS * 60) and (not finished) and (T[0].lives > 0): #основной цикл первой части игры
    clock.tick(FPS)
    
    for i in range(5):
        if s[i] == 0: #блок создания нового мяча
            s[i] = Ball(randint(100, 900), randint(100, 500),  randint(10, 50), 0,
            COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)], 0, 0)
        
    if (w > 150) and (s[5] == 0):#блок создания особого мяча
        s[5] = Ball(randint(100, 900), randint(100, 500),  randint(30, 50), 0,
        COLORS[randint(0, 5)], a[randint(0, len(a)-1)], a[randint(0, len(a)-1)], 1, 0)
        
    if w % 20 == 0: #блок создания бомб
        bombs.append(Bombs(randint(5, 495), 5, 5, 5, RED, 0, randint(5, 10), 5, 0))
        
    for i in s: #блок реализации перемещения мячей
        if i != 0:
            i.move_ball(screen, w)
            i.ball_collision(s)
            i.wall_collision() 
                    
    for i in bombs: #блок реализации перемещения бомб
        i.move_ball(screen, w)
        
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if event.type == pygame.QUIT:#выхода из игры
            finished = True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:#нажатие на кнопку мыши
            x = pygame.mouse.get_pos()[0] #определяем координаты положения мыши
            y = pygame.mouse.get_pos()[1]
            if (x >= 900) and (y <= 30):
                for i in range (2):
                    T[i].lives = 3
                    T[i].shells = [0]*4
                    T[i].buckshot = 0
                    T[i].m = 0
                    w = 0
        elif event.type == pygame.KEYDOWN: #нажатие на клавиши
            if event.key == pygame.K_SPACE:
                T[0].press[0] = True
            if event.key == pygame.K_LSHIFT:
                T[0].shooting_with_buckshot = not (T[0].shooting_with_buckshot)
            if event.key == pygame.K_LEFT:
                T[0].press[1] = True
            if event.key == pygame.K_RIGHT:
                T[0].press[2] = True
            if event.key == pygame.K_UP:
                T[0].press[3] = True
            if event.key == pygame.K_DOWN:
                T[0].press[4] = True
        elif event.type == pygame.KEYUP: #отпускание клавиш
            if event.key == pygame.K_SPACE:
                T[0] = shout(T[0])
                T[0].l = 50
                T[0].press[0] = False
            if event.key == pygame.K_LEFT:
                T[0].press[1] = False
            if event.key == pygame.K_RIGHT:
                T[0].press[2] = False
            if event.key == pygame.K_UP:
                T[0].press[3] = False
            if event.key == pygame.K_DOWN:
                T[0].press[4] = False
    
    #блок обработки выполненных противником действий
    T[1].press[0] = True
    time = np.sin(np.pi/60*w)
    if time > 0:
        T[1].press[3] = True
    elif time < 0:
        T[1].press[4] = True
    if w % 60 == 0:
        T[1].press[3] = False
        T[1].press[4] = False
    if w % 30 == 29:
        T[1] = shout(T[1])
        T[1].l = 50
        T[1].press[0] = False
     
    for k in range(2): #блок реализации перемещения танков их их столкновения с бомбами
        T[k].move_tank(screen, w)
        for i in range(len(bombs)):
            T[k].lives = bombs[i].collision_bombs_with_tanks(T[k].location, T[k].number, T[k].lives)
            
    bombs = update_bombs(bombs) #обновляем список бомб
            
    if T[0].m >= len(T[0].shells): #выводим на экран предупреждение - пушка игрока перезаряжается и стрелять не может
        screen.blit(recharge, (300, 0))
    
    for k in range (2):
        for v in range(T[k].m): #блок реализации перемещения ядер и их столкновений с мячами
            T[k].shells[v].move_ball(screen, w)
            T[k].shells, s, T[k].lives = T[k].shells[v].critical_collision(T[k].shells, s, T[k].lives, v)
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
        
    T = shell_collisions (T) #реализуем столкновения ядер между собой
    for k in range (2):
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
    
    for i in range(4): #реализуем столкновение ядер с танком и с барьером
        if T[1].shells[i] != 0:
            T[1].shells[i], T[0].lives = hit (T[0].border, T[1].shells[i], T[0].lives, 1)
            T[1].shells[i] = collision_with_barrier(T[1].shells[i])
        if T[0].shells[i] != 0:   
            T[0].shells[i], T[1].lives = hit (T[1].border, T[0].shells[i], T[1].lives, 1)
            T[0].shells[i] = collision_with_barrier(T[0].shells[i])
    
    for k in range (2):
        for i in range (T[k].m): #блок реализации столкновений ядер со стенами
            T[k].shells[i].critical_wall_collision()
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
        if T[k].buckshot != 0: #блок реализации поведения снарядов картечного типа
            if T[k].buckshot.explosion == False: #еще неразорвавшегося снаряда
                T[k].buckshot.move_ball(screen, w)
                T[k].buckshot = collision_with_barrier(T[k].buckshot)
                T[k].buckshot = collision_buckshot_with_wall(T[k].buckshot)
                y, s, T[k].lives = T[k].buckshot.critical_collision([T[k].buckshot], s, T[k].lives, 0)
                T[k].buckshot = y[0]
                T = collision_buckshot_with_other_shells(T, k)
                if T[k].buckshot.t == 30:
                    T[k].buckshot = explosion_of_buckshot(T[k].buckshot)
            else: #разорвавшегося снаряда
                T[k].buckshot.t = T[k].buckshot.t + 1
                for i in range(7):
                    if T[k].buckshot.children[i] != 0:
                        T[k].buckshot.children[i].move_ball(screen, w)
                        T[k].buckshot.children[i] = collision_with_barrier(T[k].buckshot.children[i])
                        T[k].buckshot.children[i].critical_wall_collision()
                        T[k].buckshot.children, s, T[k].lives = \
                        T[k].buckshot.children[i].critical_collision(T[k].buckshot.children, s, T[k].lives, i)
            if T[k].buckshot.t == 60:
                T[k].buckshot = 0
    
    screen.blit(Restart, (900, 0)) #рисуем кнопку рестарта
    Your_lives = create_label('Your lives - ' + str(T[0].lives), 30, 200, 30, False, False)
    #отображаем текущее кол-во жизней у игрока на экране
    screen.blit(Your_lives,(100, 0))
    Enemy_lives = create_label('Enemy lives - ' + str(T[1].lives), 30, 200, 30, False, False)
    #отображаем текущее кол-во жизней у игрока на экране
    screen.blit(Enemy_lives,(700, 0))
     
    pygame.draw.line(screen, BLACK, (0, 30), (1000, 30), 5) #рисуем верхнюю грань обл. движения шаров
    pygame.draw.circle(screen, (100, 100, 100), (500, 600), 80) #рисуем барьер
    
    w = w + 1
    
    pygame.display.update()
    screen.fill(WHITE)

T[0].shooting_with_buckshot = False
lives = [0]*2
for k in range(2):
    lives[k] = T[k].lives #сохраняем промежуточные результаты

while (not finished) and (T[0].lives > 0) and (T[1].lives > 0) and (w <= FPS * 120): #основной цикл второй части игры
    clock.tick(FPS)
    
    if w % 20 == 0: #блок создания бомб
        bombs.append(Bombs(randint(5, 495), 5, 5, 5, RED, 0, randint(5, 10), 5, 0))
        
    for i in bombs: #блок реализации перемещения бомб
        i.move_ball(screen, w)
    
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if event.type == pygame.QUIT:#выхода из игры
            finished = True
            break
        elif event.type == pygame.MOUSEBUTTONDOWN:#нажатие на кнопку мыши
            x = pygame.mouse.get_pos()[0] #определяем координаты положения мыши
            y = pygame.mouse.get_pos()[1]
            if (x >= 900) and (y <= 30):
                for k in range(2):
                    T[k].lives = lives[k]
                    T[k].shells = [0]*4
                    T[k].buckshot = 0
                    T[k].m = 0    
                w = FPS * 60
        elif event.type == pygame.KEYDOWN: #оьработка нажатий на клавиши
            if event.key == pygame.K_SPACE:
                T[0].press[0] = True
            if event.key == pygame.K_LEFT:
                T[0].press[1] = True
            if event.key == pygame.K_RIGHT:
                T[0].press[2] = True
            if event.key == pygame.K_UP:
                T[0].press[3] = True
            if event.key == pygame.K_DOWN:
                T[0].press[4] = True
        elif event.type == pygame.KEYUP: #обработка отпускания клавиш
            if event.key == pygame.K_SPACE:
                T[0] = shout(T[0])
                T[0].l = 50
                T[0].press[0] = False
            if event.key == pygame.K_LEFT:
                T[0].press[1] = False
            if event.key == pygame.K_RIGHT:
                T[0].press[2] = False
            if event.key == pygame.K_UP:
                T[0].press[3] = False
            if event.key == pygame.K_DOWN:
                T[0].press[4] = False
    
    #блок обработки выполненных противником действий
    T[1].press[0] = True
    time = np.sin(np.pi/60*w)
    if time > 0:
        T[1].press[3] = True
    elif time < 0:
        T[1].press[4] = True
    if w % 60 == 0:
        T[1].press[3] = False
        T[1].press[4] = False
    if w % 30 == 29:
        T[1] = shout(T[1])
        T[1].l = 50
        T[1].press[0] = False
        
    for k in range(2): #блок реализации перемещения танков  
        T[k].move_tank(screen, w)
        for i in range(len(bombs)):
            T[k].lives = bombs[i].collision_bombs_with_tanks(T[k].location, T[k].number, T[k].lives)
            
    bombs = update_bombs(bombs) #обновляем список бомб
     
    if T[0].m >= len(T[0].shells): #выводим на экран предупреждение - пушка игрока перезаряжается и стрелять не может
        screen.blit(recharge, (300, 0))
        
    screen.blit(Restart, (900, 0)) #рисуем кнопку рестарта
    Your_lives = create_label('Your lives - ' + str(T[0].lives), 30, 200, 30, False, False)
    #отображаем текущее кол-во жизней у игрока на экране
    screen.blit(Your_lives,(100, 0))
    Enemy_lives = create_label('Enemy lives - ' + str(T[1].lives), 30, 200, 30, False, False)
    #отображаем текущее кол-во жизней у противника на экране
    screen.blit(Enemy_lives,(700, 0))
    
    for k in range (2):
        for v in range(T[k].m): #блок реализации перемещения ядер
            T[k].shells[v].move_ball(screen, w)
        
    T = shell_collisions (T) #реализуем столкновения ядер между собой
    for k in range (2):
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
    
    for i in range(4): #реализуем попадание в танк
        if T[1].shells[i] != 0:
            T[1].shells[i], T[0].lives = hit (T[0].border, T[1].shells[i], T[0].lives, 2)
        if T[0].shells[i] != 0:   
            T[0].shells[i], T[1].lives = hit (T[1].border, T[0].shells[i], T[1].lives, 2)
        
    for k in range (2): #обновляет список ядер
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
        
    for k in range(2): #реализуем столкновения ядер с барьером
        for i in range(4):
            T[k].shells[i] = collision_with_barrier(T[k].shells[i])
        
    for k in range (2):
        for i in range (T[k].m): #блок реализации столкновений ядер со стенами
            T[k].shells[i].critical_wall_collision()
        T[k].shells, T[k].m = updates(T[k].shells, T[k].m)
              
    pygame.draw.line(screen, BLACK, (0, 30), (1000, 30), 5) #рисуем верхнюю грань обл. движения шаров
    pygame.draw.circle(screen, (100, 100, 100), (500, 600), 60) #рисуем барьер
    w = w + 1
    pygame.display.update()
    screen.fill(WHITE)
    
if (T[0].lives <= 0) or (finished == True): #блок вывода результата игры на экран  
    score = 'ПОРАЖЕНИЕ'
elif T[1].lives <= 0:
    score = '  ПОБЕДА'
else:
    score = '  НИЧЬЯ'

result = create_label(score, 80, 400, 80, False, False)
screen.blit(result, (300, 260))   
pygame.display.update()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():#блок обработки выполненных игроком действий
        if (event.type == pygame.QUIT) or (event.type == pygame.MOUSEBUTTONDOWN):#выхода из игры
            finished = True
    
pygame.quit()       
            
            
            
            
            
            
            
 
                
              
            
            
            
            
            
            
 
                
    