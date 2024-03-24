#создай игру "Лабиринт"!
from pygame import *


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
'''class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and x > 5:
            x -= speed
        if keys_pressed[K_d]and x < 595:
            x += speed
        if keys_pressed[K_w] and y > 5:
            y -= speed
        if keys_pressed[K_s] and y < 395:
            y += speed'''

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_a] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys_pressed[K_d]and self.rect.x < 595:
            self.rect.x += self.speed
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 395:
            self.rect.y += self.speed
class Enemy(GameSprite):
    def update(self):
        if self.rect.x <= 470:
            self.direction = 'right'
        if self.rect.x >= win_width - 85:
                self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed      
class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y    
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


window = display.set_mode((700,500))
display.set_caption('Maze')
background = transform.scale(image.load('background.jpg'), (700, 500))
win_height = 500
win_width = 700
hero = Player('hero.png', 5, win_height - 80,4)
cyborg = Enemy('cyborg.png', win_width - 80, 280, 2)
treasure = GameSprite('treasure.png',win_width -100, win_height -80, 0)
w1 = Wall(154, 205, 50,100, 200, 450, 10)
w2 = Wall(154, 205, 50, 100, 480, 350, 10)
w3 = Wall(154, 205, 50, 100, 200, 10, 380)
  
FPS = 60
clock = time.Clock()
finish = False
game = True
x = 600
y = 250
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
font.init()



font = font.Font(None, 70)
win = font.render('YOU WIN! ', True, (255, 215, 0))
lose = font.render('YOU LOSE!', True, (180, 0, 0))

money = mixer.Sound('money.ogg')
kick = mixer.Sound('kick.ogg')
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0, 0))
        hero.reset()
        cyborg.reset()
        treasure.reset()
        hero.update()
        cyborg.update()
        w1.draw_wall()
        w2.draw_wall()
        w3.draw_wall()
        if sprite.collide_rect(hero, cyborg) or sprite.collide_rect(hero, w1) or sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3):
            finish = True
            kick.play()
            window.blit(lose,(200, 200))

        if sprite.collide_rect(hero,treasure):
            finish = True
            money.play()
            window.blit(win,(200, 200))
    clock.tick(FPS)
    display.update()