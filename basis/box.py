import pygame
import sys
import numpy
from pygame.locals import *

pygame.init()#游戏初始化
game_display=pygame.display.set_mode((800,600))#游戏界面
pygame.display.set_caption("Our Game")
def event_handler():
    for event in pygame.event.get():
        print(event)
        if event.type == QUIT or (event.type==KEYDOWN and (event.key ==K_ESCAPE or event.key==K_q)):
            pygame.quit()
            quit()
while True:#游戏主循环
    event_handler()#获取按键，判断是否退出

    pygame.display.update()#刷新游戏界面