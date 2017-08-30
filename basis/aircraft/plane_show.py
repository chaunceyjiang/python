import pygame
from pygame.locals import *

plane_img=pygame.image.load('resources/image/shoot.png')
background_img=pygame.image.load('resources/image/background.png')
player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家精灵图片区域
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(167, 750, 167, 258))     # 玩家爆炸精灵图片区域
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
enemy1_rect = pygame.Rect(534, 612, 57, 40)
enemy1_img = plane_img.subsurface(enemy1_rect)
pygame.init()
screen = pygame.display.set_mode((480, 800), 0, 32)
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    screen.blit(background_img,(0,0))

    screen.blit(plane_img.subsurface(player_rect[2]), (0, 0))

    pygame.display.update()