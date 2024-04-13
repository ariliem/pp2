import pygame, sys
import time
from pygame.locals import *
import random

pygame.init()
FPS = pygame.time.Clock()
FPS.tick(60)

BLUE = (0,0,255)
RED = (255,0,0)
GREEN = (0,255,0)
BLACK = (0,0,0)
WHITE = (255,255,255)
WIDTH = 400
HEIGHT = 600
SPEED = 5
SCORE = 0
COINSPEED = 5
COINS = 0
LEVEL = 1

font = pygame.font.Font(None, 60)
game_over = font.render("Game over", True, BLACK)

background = pygame.image.load("resources/street.png")
background = pygame.transform.scale(background, (WIDTH, HEIGHT))
display = pygame.display.set_mode((WIDTH, HEIGHT))
display.fill(WHITE)

pygame.display.set_caption("Racer")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/playy.png")
        self.image = pygame.transform.scale(self.image, (48,93))
        self.rect = self.image.get_rect()
        self.rect.center = (160,520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0,5)
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5,0)
        if self.rect.right < WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5,0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("resources/enemyy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH-40),0)

    def move(self):
        global SCORE
        self.rect.move_ip(0,SPEED)
        if (self.rect.top > 600):
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)
        def move(self):
            global COINS
            elf.rect.move_ip(0,COINSPEED)
            if (self.rect.bottom > 600):

                self.rect.top = 0
                self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.randomCoin = random.randint(1,3)
        self.image = pygame.image.load(f"resources/coin{self.randomCoin}.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, WIDTH - 40),0)

    def move(self):
        global COINS
        self.rect.move_ip(0,COINSPEED)
        if (self.rect.bottom > 600): 
            self.rect.top = 0
            self.rect.center = (random.randint(40, WIDTH - 40), 0)

ply = Player()
enm = Enemy()
coin = Coin()
coin_dup = 0
enemies = pygame.sprite.Group()
enemies.add(enm)
coins = pygame.sprite.Group()
coins.add(coin)
all_sprites = pygame.sprite.Group()
all_sprites.add(ply)
all_sprites.add(enm)
all_sprites.add(coin)

def levels():
    global LEVEL
    global SPEED
    if COINS//4>LEVEL:
        LEVEL += 1
        SPEED += 3

inc_speed = pygame.USEREVENT + 1
pygame.time.set_timer(inc_speed, 1000)
run = True
game_paused = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == inc_speed:
            SPEED += 0.5

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_paused = not game_paused  # Toggle pause state

    if not game_paused:
        levels()

        display.blit(background, (0, 0))  # Blit the background before filling with white color
        scores = font.render(str(SCORE), True, BLACK)
        display.blit(scores, (10,10))
        collected = font.render(str(COINS), True, BLACK)
        display.blit(collected, (400-30,10))
        levelss = font.render(str(LEVEL), True, BLACK)
        display.blit(levelss, (400-30, 400-30))

        for entity in all_sprites:
            display.blit(entity.image, entity.rect)
            entity.move()

        if pygame.sprite.spritecollideany(ply, enemies):
            pygame.mixer.Sound("resources/crash.wav").play()
            time.sleep(0.5)
              
            display.fill(RED)
            display.blit(game_over, (100,250))
            pygame.display.update()
            for ent in all_sprites:
                ent.kill() 
            time.sleep(1)
            pygame.quit()
            sys.exit() 
        if pygame.sprite.spritecollideany(ply, coins):
                for coin in coins:
                    coin.kill()

                if coin.randomCoin == 1:
                    COINS += 1
                if coin.randomCoin == 2:
                    COINS += 2
                if coin.randomCoin == 3:
                    COINS += 3
                pygame.display.update()
        if(len(coins) == 0): # if our coin was collected:
            COIN = Coin()   # new coin object will be created and added to the coins group
            coins.add(COIN)
            all_sprites.add(COIN)

    pygame.display.flip()
    FPS.tick(30)
