import pygame
from pygame.locals import *
pygame.init()
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
background=pygame.image.load("mouse.png")
x,y=0,0
dx,dy=0,0
while True:
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            quit()
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                dx=-1
            if event.key == K_RIGHT:
                dx=1
            if event.key == K_UP:
                dy=-1
            if event.key == K_DOWN:
                dy=1
        elif event.type == KEYUP:
            dx=0
            dy=0

    if x >=0 and x<SCREEN_SIZE[0]:
        x += dx
    if y >=0 and y< SCREEN_SIZE[1]:
        y += dy
    screen.fill((0,0,0))
    screen.blit(background,(x,y))
    pygame.display.update()
