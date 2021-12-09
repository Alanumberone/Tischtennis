from pygame import *
from random import randint


game = True
finish = False
FPS = 60
clock = time.Clock()
clock.tick(FPS)
font.init()
font = font.SysFont('Arial', 30)

class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed,x_size,y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size,y_size))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y< 495:
            self.rect.y+=self.speed
        if keys_pressed[K_s] and self.rect.y> 5:
            self.rect.y-=self.speed
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y< 495:
            self.rect.y+=self.speed
        if keys_pressed[K_DOWN] and self.rect.x> 5:
            self.rect.y-=self.speed

class Ball(GameSprite):
    def update(self):
        pass

win = display.set_mode((700,500))
display.set_caption('PONG')
background = transform.scale(image.load('Blck bckgrnd.png'),(700,500))

player1 = Player('pong villager.png',100,100,3,100,200)

while game:
    import time
    for e in event.get():
        if e.type == QUIT:
            game = False
        else:
            pass
    if finish != True:
        pass
    display.update()
    clock.tick(FPS)