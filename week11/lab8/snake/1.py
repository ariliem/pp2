import pygame
from pygame.math import Vector2
import time
import random 



class Snake:
    def __init__(self):
        self.body = [Vector2(7, 10), Vector2(6, 10), Vector2(5, 10)]
        self.eated = False
        self.isDead = False

    def drawingSnake(self):
        for block in self.body:
            body_rect = pygame.Rect(block.x * cell_size, block.y * cell_size, cell_size, cell_size)
            pygame.draw.rect(screen, (0 ,128 ,0), body_rect)

    def snakeMoving(self):
        if self.eated == True:
            body_copy = self.body[:]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]
            self.eated = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0, body_copy[0] + direction)
            self.body = body_copy[:]


class Fruit:
    def __init__(self):
        self.randomize()
    
    def drawingFruit(self):
        fruit_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        # pygame.draw.rect(screen, (107 ,142 ,35), fruit_rect)
        screen.blit(apple, fruit_rect)

    def randomize(self):
        self.x = random.randint(0, cell_number - 2)
        self.y = random.randint(0, cell_number - 2)
        self.pos = Vector2(self.x, self.y)

class Game:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.level = 1
        self.snake_speed = 5
        # self.isDead = False

    def update(self):
        self.snake.snakeMoving()
        self.checkCollision()
        # self.levelAdding()

    def drawElements(self):
        self.snake.drawingSnake()
        self.fruit.drawingFruit()
        self.scoreDrawing()
    
    def checkCollision(self):
        if(self.fruit.pos == self.snake.body[0]):
            self.snake.eated = True
            self.fruit.randomize()
            self.levelAdding()

    def gameOver(self):
        if self.snake.body[0].x >= 19:
            return True
        if self.snake.body[0].x <= 0:
            return True
        if self.snake.body[0].y >= 19:
            return True
        if self.snake.body[0].y <= 0:
            return True
        
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                return True
        return False
    
    def levelAdding(self):
        if(len(self.snake.body) - 3) % 3 == 0:
            self.level += 1
            self.snake_speed += 1
    
    def scoreDrawing(self):
        score_text = "Score: " + str(len(self.snake.body) - 3)
        score_surface = font.render(score_text, True, (56, 74, 12))
        score_rect = score_surface.get_rect(center = (cell_size * cell_number - 120, 40))
        screen.blit(score_surface, score_rect)

        level_text = "Level: " + str(self.level)
        level_surface = font.render(level_text, True, (56, 74, 12))
        level_rect = level_surface.get_rect(center = (cell_size * cell_number - 120, 70))
        screen.blit(level_surface, level_rect)



pygame.init()
clock = pygame.time.Clock()
cell_size = 40
cell_number = 20
direction = Vector2(1, 0)
screen = pygame.display.set_mode((cell_size * cell_number, cell_size * cell_number)) # creating screen with are 800x800 or 20x20 cells square
done = False

apple = pygame.image.load('apple.png').convert_alpha()
apple = pygame.transform.scale(apple, (35, 35))

font = pygame.font.Font('font.ttf', 25)


game = Game()

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            if direction.x != -1:
                direction = Vector2(1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            if direction.x != 1:
                direction = Vector2(-1, 0)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_UP:
            if direction.y != 1:
                direction = Vector2(0, -1)
        if event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN:
            if direction.y != -1:
                direction = Vector2(0, 1)

    if(game.gameOver() == True):
        done = True
    
        
    screen.fill((175, 215, 70))
    game.drawElements()
    game.update()
    pygame.display.flip()
    clock.tick(game.snake_speed)
pygame.quit()