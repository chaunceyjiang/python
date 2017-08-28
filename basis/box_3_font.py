import pygame
from pygame.locals import *

pygame.init()
SCREEN_SIZE=(640,480)
screen=pygame.display.set_mode(SCREEN_SIZE,0,32)
font=pygame.font.SysFont(r'C:\Windows\Fonts\simfang.ttf',16)
font_height=font.get_linesize()
event_text=[]
while True:
    event=pygame.event.wait()
    event_text.append(str(event))
    event_text = event_text[-int(SCREEN_SIZE[1] / font_height):]
    if event.type==QUIT:
        pygame.quit()
        quit()
    y=SCREEN_SIZE[1]-font_height
    for text in reversed(event_text):
        screen.blit(font.render(text,True,(0,255,0)),(0,y))
        y-=font_height+10
    pygame.display.update()