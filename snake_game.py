import pygame #imports pygame libraries
import random #generates random actions
import sys #provides functions and variables

pygame.init() #initializes pygame modules

SW, SH = 800,800

BLOCK_SIZE = 50
FONT = pygame.font.Font("font.ttf", BLOCK_SIZE*2)

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW, BLOCK_SIZE):
        for y in range(0, SH, BLOCK_SIZE):
            rect = pygame.Rect(x,y, BLOCK_SIZE, BLOCK_SIZE)
            pygame.draw.rect(screen, "#FFFFFF", rect, 1)

class Snake:
    def __init__(self):
        self.x, self.y = BLOCK_SIZE, BLOCK_SIZE
        self.xdir = 1
        self.ydir = 0
        self.head = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
        self.body = [pygame.Rect(self.x-BLOCK_SIZE,self.y, BLOCK_SIZE, BLOCK_SIZE)]
        self.dead = False
    def update(self):
        self.body.append(self.head)
        for i in range(len(self.body)-1):
            self.body[i].x, self.body[i].y = self.body[i+1].x, self.body[i+1].y
        self.head.x += self.xdir * BLOCK_SIZE
        self.head.y += self.ydir * BLOCK_SIZE
        self.body.remove(self.head)
class Apple:
    def __init__(self):
        self.x = int(random.randint(0,SW)/BLOCK_SIZE) * BLOCK_SIZE
        self.y = int(random.randint(0, SH)/BLOCK_SIZE) * BLOCK_SIZE
        self.rect = pygame.Rect(self.x, self.y, BLOCK_SIZE, BLOCK_SIZE)
    def update(self):
        pygame.draw.rect(screen,"red", self.rect)

drawGrid()
snake = Snake()
apple = Apple()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
              snake.ydir = 1
              snake.xdir = 0
            elif event.key == pygame.K_UP:
              snake.ydir = -1
              snake.xdir = 0
            elif event.key == pygame.K_RIGHT:
              snake.ydir = 0
              snake.xdir = 1
            elif event.key == pygame.K_LEFT:
              snake.ydir = 0
              snake.xdir = -1


    snake.update()
    screen.fill('black')
    drawGrid()
    apple.update()
    pygame.draw.rect(screen, "green", snake.head)

    for square in snake.body:
        pygame.draw.rect(screen, "green", square)

    pygame.display.update()
    clock.tick(10)