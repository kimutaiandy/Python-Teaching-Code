import pygame
pygame.init()

WIDTH, HEIGHT = 700,500 #set width and height for window dynamically
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #set up window
pygame.display.set_caption("Ping Pong") #Diplays title of the window

FPS = 60 #Defining Frame rate
WHITE = (255,255,255)
BLACK = (0,0,0)

PADDLE_HEIGHT,PADDLE_WIDTH = 100,20
BALL_RADIUS = 7
class Paddle: #defining the paddle
    COLOR = WHITE
    VEL = 4
    def __init__(self,x,y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
    def draw(self, win):
        pygame.draw.rect(win, self.COLOR, (self.x, self.y, self.width, self.height))
    def move(self, up = True):
        if up:
            self.y -= self.VEL
        else:
            self.y += self.VEL

class Ball:
    MAX_VEL = 5
    COLOR = WHITE
    def __init__(self, x,y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.x_vel = self.MAX_VEL
        self.y_vel = 0

    # this is how we draw the ball
    def draw(self, win):
        pygame.draw.circle(win, self.COLOR, (self.x,self.y),self.radius)
    #this is how we move the ball
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel



def draw(win, paddles, ball):
    win.fill(BLACK)

    for paddle in paddles:
        paddle.draw(win)
#Drawing a dotted line at the centre of the screen
    for i in range(10, HEIGHT, HEIGHT//20):
        if i%2 == 1:
            continue
        pygame.draw.rect(win, WHITE, (WIDTH//2 - 5, i, 10, HEIGHT//20))
    ball.draw(win)
    pygame.display.update()

def handle_collision(ball, left_paddle,right_paddle):
    #Handles collision with the ceiling
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel *= -1 #reverses the direction of the ball
    elif ball.y - ball.radius <=0:
        ball.y_vel *= -1
    #check which paddle is being hit
    if ball.x_vel <0:
        if ball.y >= left_paddle.y and ball.y <= left_paddle.y + left_paddle.height:
            if ball.x - ball.radius <= left_paddle.x + left_paddle.width:
                ball.x_vel *= -1

                middle_y = left_paddle.y + left_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (left_paddle.height/2) / ball.MAX_VEL
                y_vel = difference_in_y /reduction_factor
                ball.y_vel = -1* y_vel

    else:
        if ball.y >= right_paddle.y and ball.y <= right_paddle.y + right_paddle.height:
            if ball.x + ball.radius >= right_paddle.x:
                ball.x_vel *= -1

                middle_y = right_paddle.y + right_paddle.height / 2
                difference_in_y = middle_y - ball.y
                reduction_factor = (right_paddle.height/2) / ball.MAX_VEL
                y_vel = difference_in_y /reduction_factor
                ball.y_vel = -1* y_vel

def handle_paddle_movement(keys, left_paddle, right_paddle):
    if keys[pygame.K_w] and left_paddle.y - left_paddle.VEL >=0:
        left_paddle.move(up=True)
    if keys[pygame.K_s] and left_paddle.y + left_paddle.VEL + left_paddle.height <= HEIGHT:
        left_paddle.move(up=False)

    if keys[pygame.K_UP] and right_paddle.y - right_paddle.VEL >=0:
        right_paddle.move(up=True)
    if keys[pygame.K_DOWN] and right_paddle.y + right_paddle.VEL + right_paddle.height <= HEIGHT:
        right_paddle.move(up=False)


def main(): #main loop of the program
    run = True
    clock = pygame.time.Clock()

    left_paddle = Paddle(10, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    right_paddle = Paddle(WIDTH - 10 - PADDLE_WIDTH, HEIGHT//2 - PADDLE_HEIGHT//2, PADDLE_WIDTH, PADDLE_HEIGHT)
    ball = Ball(WIDTH//2, HEIGHT//2, BALL_RADIUS)
    while run:
        clock.tick(FPS) #makes sure the game can't run faster than 60FPS
        draw(WIN, [left_paddle, right_paddle], ball)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: #event to quit the window
                run = False
                break
        keys = pygame.key.get_pressed()
        handle_paddle_movement(keys, left_paddle, right_paddle)
        ball.move()#moves the ball
        handle_collision(ball, left_paddle, right_paddle)
    pygame.quit()

if __name__ == '__main__': #this ensures that the main module is being run for the main function to run
    main()