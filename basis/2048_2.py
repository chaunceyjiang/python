import numpy as np
import random
GRID=4
score=0
def init_matrix():#初始矩阵
    return np.random.randint(3,size=[GRID,GRID])*2
matrix=init_matrix()
def newrandom(matrix):
    x,y=np.where(matrix==0)
    t= 4 if random.random() >= 0.7 else 2
    L=list(zip(x,y))
    if len(L)>0:
        index=random.choice(L)
        matrix[index[0],index[1]]=t
    return matrix
def removeZero(matrix,action):#根据action direction 移除 zero
    zeros=np.zeros([GRID,GRID])
    t=0
    if direction == 'w':
        matrix1=matrix.T
        for i in matrix1:
            L=i.tolist()
            if len(L) >0 and max(L) >0:
                while min(L)==0:L.remove(0)
            zeros[t]=addSequence(L,"l")
            t += 1
        return zeros.T
    if direction == 'a':
        for i in matrix:
            L=i.tolist()
            if len(L) > 0 and max(L) > 0:
                while min(L)==0:L.remove(0)
            m=addSequence(L,"l")
            zeros[t]=m
            t+=1
        return zeros
    if direction == 's':
        matrix2 = matrix.T
        for i in matrix2:
            L=i.tolist()
            if len(L) > 0 and max(L) > 0:
                while min(L)==0:L.remove(0)
            zeros[t]=addSequence(L,"r")
            t += 1
        return zeros.T
    if direction == 'd':
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
while True:
    print(matrix)
    score=matrix.sum()*matrix.max()
    print(score)
    direction=input()
    matrix=removeZero(matrix,direction)
    matrix=newrandom(matrix)

