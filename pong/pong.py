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
    def __init__(self,player_image,player_x,player_y,player_speed_x,player_speed_y,x_size,y_size):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(x_size,y_size))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = player_speed_x
        self.speed_y = player_speed_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))

class Player(GameSprite):
    def update1(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_s] and self.rect.y< 400:
            self.rect.y+=self.speed_y
        if keys_pressed[K_w] and self.rect.y> 0:
            self.rect.y-=self.speed_y
    def update2(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_DOWN] and self.rect.y< 400:
            self.rect.y+=self.speed_y
        if keys_pressed[K_UP] and self.rect.y> 0:
            self.rect.y-=self.speed_y

class Ball(GameSprite):
    def update(self):
        pass

win = display.set_mode((700,500))
display.set_caption('PONG')

player1 = Player('racket.png',50,200,5,5,40,100)
player2=Player('racket.png',600,200,5,5,40,100)

ball = Ball('tenis_ball.png',325,225,3,3,50,50)

attempts = 4

while game:
    import time
    for e in event.get():
        if e.type == QUIT:
            game = False
        else:
            pass
    if finish != True:
        win.fill((255,255,255))
        ball.rect.x += ball.speed_x
        ball.rect.y += ball.speed_y
        if sprite.collide_rect(player1, ball) or sprite.collide_rect(player2, ball):
            ball.speed_x *= -1
        if ball.rect.y <= 0 or ball.rect.y >= 450:
            ball.speed_y *= -1
        if ball.rect.x <= 0:
            player1_lost = font.render('Player 1 lost!',True,(175,0,0))
            win.blit(player1_lost,(275,230))
            finish = True
        if ball.rect.x >= 650:
            player2_lost = font.render('Player 2 lost!',True,(175,0,0))
            win.blit(player2_lost,(275,230))
            finish = True
        player1.update1()
        player1.reset()
        player2.update2()
        player2.reset()
        ball.update()
        ball.reset()
    keys_pressed = key.get_pressed()
    if keys_pressed[K_r] and attempts >0:
        ball.rect.x =325
        ball.rect.y =225
        player1.rect.y =200
        player2.rect.y =200
        attempts -= 1
        finish = False
    display.update()
    clock.tick(FPS)