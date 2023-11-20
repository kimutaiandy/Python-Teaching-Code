import pygame
pygame.init()

WIDTH, HEIGHT = 700,500 #set width and height for window dynamically
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #set up window
pygame.display.set_caption("Ping Pong") #Diplays title of the window

FPS = 60 #Defining Frame rate
WHITE = (255,255,255)
BLACK = (0,0,0)
def draw(win):
    win.fill(WHITE)
    pygame.display.update()
def main(): #main loop of the program
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS) #makes sure the game can't run faster than 60FPS
        draw(WIN)
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #event to quit the window
                run = False
                break
    pygame.quit()

if __name__ == '__main__': #this ensures that the main module is being run for the main function to run
    main()