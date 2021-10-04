import pygame as p

p.init()

FPS = 30
screen = p.display.set_mode((400, 400))
screen.fill((200, 200, 200))
p.draw.circle(screen, (255, 255, 0), (200, 200), 50)
p.draw.circle(screen, (0, 0, 0), (200, 200), 50, 5)
p.draw.circle(screen, (255, 0, 0), (175, 190), 12)
p.draw.circle(screen, (0, 0, 0), (175, 190), 6)
p.draw.circle(screen, (255, 0, 0), (225, 190), 12)
p.draw.circle(screen, (0, 0, 0), (225, 190), 6)
p.draw.rect(screen, (0, 0, 0), (170, 220, 60, 10))
p.draw.line(screen, (0, 0, 0), (140,160), (184,182), 5)
p.draw.line(screen, (0, 0, 0), (216,178), (260,160), 5)


p.display.update()
clock = p.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in p.event.get():
        if event.type == p.QUIT:
            finished = True

pygame.quit()