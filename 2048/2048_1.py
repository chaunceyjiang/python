import numpy as np
import pygame,random
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((460,600),0,32)
GRID_COLOR=(208,193,180)
BACKGROUND_COLOR=(187,173,160)
GAMW_BACKGROUND=(250,248,239)
GRID=4;GRID_LEN=100;SOUCRE=0;GRID_INTERVAL = 10;OVER=False
GRID_COLOR = {
        0:(208,193,180),2:(255,255,255),4:(237,224,200),
        8:(242,177,121),16:(255,220,128),32:(246,124,95),
        64:(255,190,0),128:(255,160,0),256:(255,130,0),
        512:(255,100,0),1024:(255,70,0),2048:(255,40,0),
        4096:(255,10,0),8192:(255,153,110),16384:(255,16,100)
}
font=pygame.font.SysFont(r'C:\Windows\Fonts\simfang.ttf',45)
font2=pygame.font.SysFont(r'C:\Windows\Fonts\simfang.ttf',60)
font3=pygame.font.SysFont(r'C:\Windows\Fonts\simfang.ttf',45)
def init_matrix():#初始矩阵
    return np.random.randint(3,size=[GRID,GRID],dtype=int)*2
matrix=init_matrix()
def newrandom(matrix):
    x,y=np.where(matrix==0)
    t= 4 if random.random() >= 0.95 else 2
    L=list(zip(x,y))
    if len(L)>0:
        index=random.choice(L)
        matrix[index[0],index[1]]=t
    return matrix
def removeZero(matrix,action):#根据action direction 移除 zero
    zeros=np.zeros([GRID,GRID],dtype=int)
    t=0
    if action == 'w':
        matrix1=matrix.T
        for i in matrix1:
            L=i.tolist()
            if len(L) >0 and max(L) >0:
                while min(L)==0:L.remove(0)#移除元素0
            zeros[t]=addSequence(L,"l")
            t += 1
        return zeros.T
    if action == 'a':
        for i in matrix:
            L=i.tolist()
            if len(L) > 0 and max(L) > 0:
                while min(L)==0:L.remove(0)
            m=addSequence(L,"l")
            zeros[t]=m
            t+=1
        return zeros
    if action == 's':
        matrix2 = matrix.T
        for i in matrix2:
            L=i.tolist()
            if len(L) > 0 and max(L) > 0:
                while min(L)==0:L.remove(0)
            zeros[t]=addSequence(L,"r")
            t += 1
        return zeros.T
    if action == 'd':
        for i in matrix:
            L=i.tolist()
            if len(L) > 0 and max(L) > 0:
                while min(L)==0:L.remove(0)
            zeros[t]=addSequence(L,"r")
            t += 1
        return zeros
def addSequence(List,action):#根据action direction 合并 相邻的相同元素
    if action == 'r':
        for i in range(len(List)-1,0,-1):
            if List[i] == List[i-1]:
                List[i]*=2
                List[i-1]=0
        if max(List) > 0:
            while min(List) == 0: List.remove(0)
            List.reverse()
            List.extend([0]*(GRID-len(List)))
            List.reverse()
        return List
    if action == 'l':
        for i in range(len(List) - 1):
            if List[i] == List[i +1]:
                List[i] *= 2
                List[i + 1] = 0
        if max(List) > 0:
            while min(List) == 0: List.remove(0)
            List.extend([0] * (GRID - len(List)))
        return List
def drwa_grid(screen):
    background=pygame.surface.Surface((460, 460))
    background.fill(BACKGROUND_COLOR)
    for x in range(4):
        for y in range(4):
            pygame.draw.rect(background, GRID_COLOR[matrix[x,y]], [12+112*y,12+112*x, 102, 102])
            font_color=(0,0,0) if GRID_COLOR[matrix[x,y]][1]>150 else (255,255,255)
            if matrix[x,y]==0: font_color=(208,193,180)
            background.blit(font.render(str(matrix[x,y]),True,font_color),(12+112*y+25-8*(len(str(matrix[x,y]))-3),12+112*x+40))
    screen.blit(background, (0, 140))
def game_over(screen):
    background = pygame.surface.Surface((460, 460))
    background.fill((187,173,160,50))
    background.blit(font2.render("GAME OVER",True,(0,0,0)),(110,210))
    screen.blit(background,(0,140))
def draw_source(SOUCRE):
    background = pygame.surface.Surface((400, 140))
    background.fill(GAMW_BACKGROUND)
    background.blit(font3.render("SOURCE: %s" % SOUCRE, True, (0, 0, 0)), (50, 50))
    screen.blit(background, (0, 0))
matrix=init_matrix()
while True:
    for event in pygame.event.get():
        if event.type ==QUIT or (event.type==KEYDOWN and (event.key ==K_ESCAPE or event.key==K_q)):
            pygame.quit()
            quit()
        if event.type==KEYUP and event.key== K_a:
            matrix1 = removeZero(matrix, 'a')
            if np.equal(matrix,matrix1).all() and matrix1.min()!=0:
                OVER=True
            else:
                matrix =matrix1
            matrix = newrandom(matrix)
        if event.type==KEYUP and event.key== K_s:
            matrix1 = removeZero(matrix, 's')
            if np.equal(matrix,matrix1).all() and matrix1.min()!=0:
                OVER=True
            else:
                matrix = matrix1
            matrix = newrandom(matrix)
        if event.type==KEYUP and event.key== K_w:
            matrix1 = removeZero(matrix, 'w')
            if np.equal(matrix,matrix1).all() and matrix1.min()!=0:
                OVER=True
            else:
                matrix =matrix1
            matrix = newrandom(matrix)
        if event.type==KEYUP and event.key== K_d:
            matrix1 = removeZero(matrix, 'd')
            if np.equal(matrix,matrix1).all() and matrix1.min()!=0:
                OVER=True
            else:
                matrix =matrix1
            matrix = newrandom(matrix)
    screen.fill(GAMW_BACKGROUND)
    drwa_grid(screen)
    if OVER == True:
        game_over(screen)#画出游戏结束界面
    SOUCRE=matrix.sum()*matrix.max()
    draw_source(SOUCRE)#画出分数
    pygame.display.update()#更新画面