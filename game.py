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
        self.direction = "left"

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, image_name, speed, pos_x, pos_y, size_x, size_y):
        super().__init__(image_name, speed, pos_x, pos_y, size_x, size_y)

        self.magazine = 5
        self.reloading = False
        self.reloading_start = 1

    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 70:
            self.rect.x += self.speed
        if self.reloading:
            current_time = int(timer())
            if current_time - self.reloading_start > 3:
                self.magazine = 5

bckgrnd_clr = (200,255,255)
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(bckgrnd_clr)
display.set_caption("Game")

FPS = 120
clock = time.Clock()
run = True
finish = False


while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if not finish:
        window.fill(bckgrnd_clr)
    
    clock.tick(FPS)
    display.update()