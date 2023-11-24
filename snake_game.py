import pygame #imports pygame libraries
import random #generates random actions
import sys #provides functions and variables

pygame.init() #initializes pygame modules

SW, SH = 800,800

BLOCK_SIZE = 50
FONT = pygame.font.Font("font.ttf", 100)

screen = pygame.display.set_mode((800,800))
pygame.display.set_caption("Snake!")
clock = pygame.time.Clock()

def drawGrid():
    for x in range(0, SW)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(10)