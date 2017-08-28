import pygame
import sys
import numpy
from pygame.locals import *


pygame.init()
display_width=800
display_height=600
screen=pygame.display.set_mode((display_width,display_height),0,32)
background_img='pygame.png'
mouse_img='fugu.png'
pygame.display.set_caption("Hello World!")

background=pygame.image.load(background_img).convert()
mouse_cursor=pygame.image.load(mouse_img).convert_alpha()
while True:
    for event in pygame.event.get():
        if event.type ==QUIT or (event.type==KEYDOWN and (event.key ==K_ESCAPE or event.key==K_q)):
            pygame.quit()
            quit()
    screen.blit(background,(0,0))
    x,y=pygame.mouse.get_pos()
    x-=mouse_cursor.get_width()/2
    y-=mouse_cursor.get_height()/2
    screen.blit(mouse_cursor,(x,y))
    pygame.display.update()