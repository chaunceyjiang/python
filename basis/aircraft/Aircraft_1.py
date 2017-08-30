import pygame,random
from pygame.locals import *

SCREEN_WIDTH=480
SCREEN_HEIGHT=800

#子弹
class Bullet(pygame.sprite.Sprite):
    def __init__(self,bullet_img,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        self.rect=self.image.get_rect()#获取矩形区域，用来检测碰撞
        self.rect.midbottom=init_pos
        self.speed=10
    def move(self):
        self.rect.top-=self.speed
#玩家
class Player(pygame.sprite.Sprite):
    def __init__(self,plane_img,player_rect,init_pos):
        pygame.sprite.Sprite.__init__(self)
        self.image=[]
        for i in range(len(player_rect)):
            self.image.append(plane_img.subsurface(player_rect[i]).convert_alpha())
        self.rect=player_rect[0]
        self.rect.topleft=init_pos
        self.speed=8
        self.bullets=pygame.sprite.Group()
        self.img_index=0
        self.is_hit=False
    def shoot(self,bullet_img):
        pos=list(self.rect.midtop)
        pos[0]+=15
        bullet1=Bullet(bullet_img,tuple(pos))
        pos[0] -= 30
        bullet2 = Bullet(bullet_img, tuple(pos))
        self.bullets.add(bullet1)
        self.bullets.add(bullet2)

    def moveUp(self):
        if self.rect.top <= 0:
            self.rect.top = 0
        else:
            self.rect.top -= self.speed

    def moveDown(self):
        if self.rect.top >= SCREEN_HEIGHT - self.rect.height:
            self.rect.top = SCREEN_HEIGHT - self.rect.height
        else:
            self.rect.top += self.speed

    def moveLeft(self):
        if self.rect.left <= 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed
    def moveRight(self):
        if self.rect.left >= SCREEN_WIDTH - self.rect.width:
            self.rect.left = SCREEN_WIDTH - self.rect.width
        else:
            self.rect.left += self.speed
class Enemy(pygame.sprite.Sprite):
    def __init__(self, enemy_img, enemy_down_imgs, init_pos,speed):
       pygame.sprite.Sprite.__init__(self)
       self.image = enemy_img
       self.rect = self.image.get_rect()
       self.rect.topleft = init_pos
       self.down_imgs = enemy_down_imgs
       self.speed = speed
       self.down_index = 0

    def move(self):
        self.rect.top += self.speed

pygame.init()

screen=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
pygame.display.set_caption("飞机大战")
background_img=pygame.image.load('resources/image/background.png').convert()
over_img=pygame.image.load('resources/image/gameover.png').convert_alpha()
plane_img=pygame.image.load('resources/image/shoot.png')

bullet_sound=pygame.mixer.Sound('resources/sound/bullet.wav')
enemy1_down_sound=pygame.mixer.Sound('resources/sound/enemy1_down.wav')
game_over_sound=pygame.mixer.Sound('resources/sound/game_over.wav')

bullet_sound.set_volume(0.3)#set the playback volume for this Sound
enemy1_down_sound.set_volume(0.3)
game_over_sound.set_volume(0.3)

pygame.mixer.music.load('resources/sound/game_music.wav')
pygame.mixer.music.play(-1)#If the loops is -1 then the music will repeat indefinitely.
pygame.mixer.music.set_volume(0.25)

player_rect = []
player_rect.append(pygame.Rect(0, 99, 102, 126))        # 玩家精灵图片区域
player_rect.append(pygame.Rect(165, 360, 102, 126))
player_rect.append(pygame.Rect(165, 234, 102, 126))     # 玩家爆炸精灵图片区域
player_rect.append(pygame.Rect(330, 624, 102, 126))
player_rect.append(pygame.Rect(330, 498, 102, 126))
player_rect.append(pygame.Rect(432, 624, 102, 126))
player_pos = [200, 600]

player = Player(plane_img, player_rect, player_pos)#初始化飞机

bullet_rect = pygame.Rect(1004, 987, 9, 21)
bullet_img = plane_img.subsurface(bullet_rect)

enemy1_rect = pygame.Rect(534, 612, 57, 40)
enemy1_img = plane_img.subsurface(enemy1_rect)
enemy1_down_imgs = []
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 347, 57, 43)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(873, 697, 57, 45)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(267, 296, 57, 48)))
enemy1_down_imgs.append(plane_img.subsurface(pygame.Rect(930, 700, 57, 45)))

enemies1 = pygame.sprite.Group()
enemies_down = pygame.sprite.Group()
shoot_frequency = 0
enemy_frequency = 0
frequency=40
player_down_index = 16

score = 0
speed = 2
clock = pygame.time.Clock()
running=True
while running:
    # 控制游戏最大帧率为60
    clock.tick(60)

    # 控制发射子弹频率,并发射子弹
    if not player.is_hit:
        if shoot_frequency % 15 == 0:  #子弹计数器
            bullet_sound.play()
            player.shoot(bullet_img)
        shoot_frequency += 1
        if shoot_frequency >= 15:
            shoot_frequency = 0
    if score> 10 :speed=3
    if score > 50 :speed=4;frequency=35
    if score > 100 :speed=6;frequency=25
    if enemy_frequency % frequency == 0:   
        enemy1_pos = [random.randint(0, SCREEN_WIDTH - enemy1_rect.width), 0]
        enemy1 = Enemy(enemy1_img, enemy1_down_imgs, enemy1_pos,speed)
        enemies1.add(enemy1)#生成敌机组
    enemy_frequency += 1
    if enemy_frequency >= 400:
        enemy_frequency = 0
    for bullet in player.bullets:
        bullet.move()
        if bullet.rect.bottom < 0:#子弹在屏幕外面，移除子弹
            player.bullets.remove(bullet)
    for enemy in enemies1:
        enemy.move()
        # 判断玩家是否被击中
        if pygame.sprite.collide_rect(enemy, player):#矩形碰撞检测
            enemies_down.add(enemy)#添加到 爆炸敌机组
            enemies1.remove(enemy)# 移除正常敌机
            player.is_hit = True
            game_over_sound.play()
            break
        if enemy.rect.top > SCREEN_HEIGHT:
            enemies1.remove(enemy)

    enemies1_down = pygame.sprite.groupcollide(enemies1, player.bullets, 1, 1)#组检测 如果敌方与子弹相撞  双方消失


    for enemy_down in enemies1_down:
        enemies_down.add(enemy_down)

    screen.fill(0)
    screen.blit(background_img, (0, 0))

    if not player.is_hit:
        screen.blit(player.image[player.img_index], player.rect)# 更换图片索引使飞机有动画效果
        player.img_index = shoot_frequency // 8
    else:
        player.img_index = player_down_index // 8
        screen.blit(player.image[player.img_index], player.rect)#被击中，更换飞机爆炸索引 动画显示
        player_down_index += 1
        if player_down_index > 47:
            running = False
    for enemy_down in enemies_down:
        if enemy_down.down_index == 0:
            enemy1_down_sound.play()
        if enemy_down.down_index > 7:#如果超过 爆炸敌机的最后一张图
            enemies_down.remove(enemy_down)
            score += 1
            continue
        screen.blit(enemy_down.down_imgs[enemy_down.down_index // 2], enemy_down.rect)#敌机爆炸效果显示
        enemy_down.down_index += 1


    player.bullets.draw(screen)
    enemies1.draw(screen)


    score_font = pygame.font.Font(None, 36)
    score_text = score_font.render(str(score), True, (128, 128, 128))
    text_rect = score_text.get_rect()
    text_rect.topleft = [10, 10]
    screen.blit(score_text, text_rect)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    # 监听键盘事件
    key_pressed = pygame.key.get_pressed()
    # 若玩家被击中，则无效
    if not player.is_hit:
        if key_pressed[K_w] or key_pressed[K_UP]:
            player.moveUp()
        if key_pressed[K_s] or key_pressed[K_DOWN]:
            player.moveDown()
        if key_pressed[K_a] or key_pressed[K_LEFT]:
            player.moveLeft()
        if key_pressed[K_d] or key_pressed[K_RIGHT]:
            player.moveRight()

font = pygame.font.Font(None, 48)
text = font.render('Score: '+ str(score), True, (255, 0, 0))
text_rect = text.get_rect()
text_rect.centerx = screen.get_rect().centerx
text_rect.centery = screen.get_rect().centery + 24
screen.blit(over_img, (0, 0))
screen.blit(text, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

