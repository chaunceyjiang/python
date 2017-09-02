import pygame
from pygame.locals import *

plane_img=pygame.image.load('resources/image/shoot.png')
background_img=pygame.image.load('resources/image/background.png')
player_rect = []
player_rect.append(pygame.Rect(68, 78, 11, 22))        # 玩家精灵图片区域
player_rect.append(pygame.Rect(840, 646, 23, 46))
player_rect.append(pygame.Rect(167, 750, 167, 258))
# 玩家爆炸精灵图片区域
player_rect.append(pygame.Rect( 267,398, 56, 86))

player_rect.append(pygame.Rect(100, 118, 63, 106))

player_rect.append(pygame.Rect(810, 692, 64, 55))

enemy1_rect = pygame.Rect(534, 612, 57, 40)
enemy1_img = plane_img.subsurface(enemy1_rect)
pygame.init()
screen = pygame.display.set_mode((480, 800), 0, 32)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background_img,(0,0))

    screen.blit(plane_img.subsurface(player_rect[0]), (0, 0))
    screen.blit(plane_img.subsurface(player_rect[4]), (300, 500))
    screen.blit(plane_img.subsurface(player_rect[5]), (400, 100))
    pygame.display.update()