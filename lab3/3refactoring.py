import pygame

pygame.init()

FPS = 30
sc = pygame.display.set_mode((600, 800))

WHITE = (255, 255, 255)   # список цветов, которые могут использоваться в рисунке
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
BLUE = (64, 128, 255)
LIGHT_BLUE = (106, 253, 254)
GREEN = (0, 200, 64)
BROWN1 = (106, 81, 0)
BROWN2 = (168, 143, 0)
kot = (250, 159, 68)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
RED = (225, 0, 0)

def okno(x, y, color01, color02):
    '''
    Функция рисует окно
    координаты x, y задают положение левого верхнего угла окна
    color01 - цвет рамы окна (LIGHT_BLUE)
    color02 - цвет стекла (BLUE)
    '''
    pygame.draw.polygon(sc, color01,
                        [[x, y], [x + 260, y],
                         [x + 260, y + 360], [x, y + 360]])
    pygame.draw.polygon(sc, color02,
                        [[x + 20, y + 20], [x + 120, y + 20],
                         [x + 120, y + 140], [x + 20, y + 140]])
    pygame.draw.polygon(sc, color02,
                        [[x + 140, y + 20], [x + 240, y + 20],
                         [x + 240, y + 140], [x + 140, y + 140]])
    pygame.draw.polygon(sc, color02,
                        [[x + 20, y + 160], [x + 120, y + 160],
                         [x + 120, y + 340], [x + 20, y + 340]])
    pygame.draw.polygon(sc, color02,
                        [[x + 140, y + 160], [x + 240, y + 160],
                         [x + 240, y + 340], [x + 140, y + 340]])

def KOT(a, x1, y1, color1, color2):
    '''
    Функция рисует кота:
    a - размер кота (при а=70, размер кота будет таким же как в задании 2)
    x1, y1 - координаты точки центра головы кота
    color1 - цвет кота
    color2 - цвет глаз кота
    '''
    b = a / 70
    pygame.draw.ellipse(sc, color1,  # хвост
                            (x1 + 290 * b, y1 - 50 * b, 280 * b, 70 * b))
    pygame.draw.ellipse(sc, BLACK,
                            (x1 + 290 * b, y1 - 50 * b, 280 * b, 70 * b), 1)
    pygame.draw.ellipse(sc, color1,  # туловище
                            (x1 - 20 * b, y1 - 100 * b, 380 * b, 200 * b))
    pygame.draw.ellipse(sc, BLACK,
                            (x1 - 20 * b, y1 - 100 * b, 380 * b, 200 * b), 1)
    pygame.draw.circle(sc, color1,  # голова
                           (x1, y1), a)
    pygame.draw.circle(sc, BLACK,
                           (x1, y1), a, 1)
    pygame.draw.ellipse(sc, color1,  # ноги
                            (x1 + 35 * b, y1 + 65 * b, 90 * b, 40 * b))
    pygame.draw.ellipse(sc, BLACK,
                            (x1 + 35 * b, y1 + 65 * b, 90 * b, 40 * b), 1)
    pygame.draw.circle(sc, color1,
                           (x1 + 330 * b, y1 + 60 * b), 60 * b)
    pygame.draw.circle(sc, BLACK,
                           (x1 + 330 * b, y1 + 60 * b), 60 * b, 1)
    pygame.draw.ellipse(sc, color1,
                            (x1 + 360 * b, y1 + 75 * b, 35 * b, 100 * b))
    pygame.draw.ellipse(sc, BLACK,
                            (x1 + 360 * b, y1 + 75 * b, 35 * b, 100 * b), 1)
    pygame.draw.circle(sc, color2,  # глаза
                           (x1 - 30 * b, y1), 15 * b)
    pygame.draw.circle(sc, BLACK,
                           (x1 - 30 * b, y1), 15 * b, 1)
    pygame.draw.circle(sc, color2,
                           (x1 + 30 * b, y1), 15 * b)
    pygame.draw.circle(sc, BLACK,
                           (x1 + 30 * b, y1), 15 * b, 1)
    pygame.draw.ellipse(sc, BLACK,
                            (x1 + 35 * b, y1 - 10 * b, 5 * b, 23 * b))
    pygame.draw.ellipse(sc, BLACK,
                            (x1 - 25 * b, y1 - 10 * b, 5 * b, 23 * b))
    pygame.draw.ellipse(sc, WHITE,
                            (x1 + 25 * b, y1 - 12 * b, 5 * b, 15 * b))
    pygame.draw.ellipse(sc, WHITE,
                            (x1 - 35 * b, y1 - 12 * b, 5 * b, 15 * b))
    pygame.draw.polygon(sc, BLACK,  # ушки
                        [[x1 - 70 * b, y1 - 65 * b], [x1 - 40 * b, y1 - 50 * b],
                         [x1 - 63 * b, y1 - 28 * b]])
    pygame.draw.polygon(sc, GRAY,
                        [[x1 - 68 * b, y1 - 63 * b], [x1 - 43 * b, y1 - 48 * b],
                         [x1 - 62 * b, y1 - 30 * b]])
    pygame.draw.polygon(sc, BLACK,
                        [[x1 + 48 * b, y1 - 70 * b], [x1 + 25 * b, y1 - 50 * b],
                         [x1 + 46 * b, y1 - 35 * b]])
    pygame.draw.polygon(sc, GRAY,
                        [[x1 + 46 * b, y1 - 68 * b], [x1 + 27 * b, y1 - 48 * b],
                         [x1 + 44 * b, y1 - 37 * b]])

    pygame.draw.polygon(sc, BLACK,  # носик
                        [[x1 - 7 * b, y1 + 23 * b], [x1 + 7 * b, y1 + 23 * b],
                         [x1, y1 + 23 * b]])
    pygame.draw.polygon(sc, GRAY,
                        [[x1 - 5 * b, y1 + 25 * b], [x1 + 5 * b, y1 + 25 * b],
                         [x1, y1 + 30 * b]])

    pygame.draw.aaline(sc, BLACK,  # усики
                       [x1 + 20 * b, y1 + 32 * b],
                       [x1 + 130 * b, y1 + 15 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1 + 20 * b, y1 + 38 * b],
                       [x1 + 130 * b, y1 + 35 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1 + 20 * b, y1 + 43 * b],
                       [x1 + 130 * b, y1 + 55 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1 - 20 * b, y1 + 31 * b],
                       [x1 - 120 * b, y1 + 15 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1 - 20 * b, y1 + 37 * b],
                       [x1 - 120 * b, y1 + 35 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1 - 20 * b, y1 + 41 * b],
                       [x1 - 120 * b, y1 + 55 * b])

    pygame.draw.aaline(sc, BLACK,  # ротик
                       [x1, y1 + 30 * b],
                       [x1 + 10 * b, y1 + 50 * b])
    pygame.draw.aaline(sc, BLACK,
                       [x1, y1 + 30 * b],
                       [x1 - 10 * b, y1 + 50 * b])
def KLUBOK(x2, y2, c):
    '''
    Функциия рисует клубок цвета GRAY
    x2, y2 - координаты точки центра клубка
    c - размеры клубка (при с=50 размеры будут такими же как в задании 2)
    '''
    d = c/50
    pygame.draw.circle(sc, GRAY,  # клубок
                       (x2, y2), c)
    pygame.draw.circle(sc, BLACK,
                       (x2, y2), c, 1)
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 - 20 * d],
                       [x2 + 30 * d, y2 + 10 * d])
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 - 10 * d],
                       [x2 + 30 * d, y2 + 30 * d])
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 - 30 * d],
                       [x2 + 30 * d, y2])
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 - 15 * d],
                       [x2 - 40 * d, y2 + 15 * d])
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 - 5 * d],
                       [x2 - 30 * d, y2 + 25 * d])
    pygame.draw.aaline(sc, BLACK,
                       [x2, y2 + 50 * d],
                       [x2 - 50 * d, y2 + 50 * d])


pygame.draw.polygon(sc, BROWN1,                      # фон
                    [[0, 0], [600, 0],
                     [600, 400], [0, 400]])
pygame.draw.polygon(sc, BROWN2,
                    [[0, 400], [600, 400],
                     [600, 800], [0, 800]])

okno(20, 20, LIGHT_BLUE, BLUE)
okno(320, 20, LIGHT_BLUE, BLUE)
KOT(10, 520, 400, GRAY, RED)
KOT(20, 400, 450, kot, GREEN)
KOT(30, 180, 500, GRAY, YELLOW)
KOT(14, 32, 550, kot, BLUE)
KOT(46, 456, 600, kot, LIGHT_BLUE)
KOT(27, 300, 680, GRAY, GRAY)
KLUBOK(40, 700, 46)
KLUBOK(50, 500, 18)
KLUBOK(270, 600, 25)
KLUBOK(350, 400, 37)
KLUBOK(50, 4500, 10)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()