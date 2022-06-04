from pygame import *
from random import randint as rnd
from time import time as timer
bullets = sprite.Group()
win_width = 700
win_height = 500
win_score = 10
window = display.set_mode((win_width, win_height))
display.set_caption("Game Shooter")
mixer.init()
#mixer.music.load("space.ogg")
#mixer.music.set_volume(0.05)
#shoot = mixer.Sound("fire.ogg")
#mixer.music.play() 
'''
background = transform.scale(
    image.load("galaxy.jpg"),
    (win_width, win_height)
    )
'''
class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, pos_x, pos_y, size_x, size_y):
        super().__init__()
        self.image = transform.scale(image.load(image_name), (size_x,size_y))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y 
        #self.direction = "left"

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_left(self):
        keys = key.get_pressed()

        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - 150:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - 150:
            self.rect.y += self.speed



bckgrnd_clr = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bckgrnd_clr)
display.set_caption("tennis")

racket_left = Player('racket.png', 4, 30, 200, 50, 150)

racket_right = Player('racket.png', 4, 620, 200, 50, 150)

ball = GameSprite('tenis_ball.png', 4, 200, 200, 50, 50)

ball_speed_x = 3
ball_speed_y = 3

font.init()
font1 = font.Font(None, 35 )
lose1 = font1.render('lose.', 0, (180,0,0))
lose2 = font1.render('lose,', 0, (180,0,0))

FPS = 50
clock = time.Clock()
run = True
finish = False


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(bckgrnd_clr)
        racket_left.update_left()
        racket_right.update_right()
    
        ball.rect.x += ball_speed_x
        ball.rect.y += ball_speed_y

        if ball.rect.y > win_height - 50 or ball.rect.y < 0:
            ball_speed_y *= -1

        if sprite.collide_rect(racket_left, ball) or sprite.collide_rect(racket_right,ball):
            ball_speed_x *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200,200))

        if ball.rect.x > win_width - 50:
            finish = True
            window.blit(lose2, (200,200))

        ball.reset()
        racket_left.reset()
        racket_right.reset()

    clock.tick(FPS)
    display.update()