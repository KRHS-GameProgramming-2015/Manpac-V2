import sys, pygame, math, random
from Ball import *
pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height 

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = .5 * 60

ballImages = ["An Actual Ghost 3.png",
			  "An Actual Ghost 2.png",
			  "An Actual Ghost.png", 
			  "An Actual Ghost 4.png"]  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
                     
        ballImage = ballImages[random.randint(0, len(ballImages)-1)]
        balls += [Ball(ballImage, ballSpeed, ballPos)]
    
    for ball in balls:
        ball.move()
        ball.collideScreen(size)
    
    for first in balls:
        for second in balls:
            if first != second:
                first.collideBall(second)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    pygame.display.flip()
    clock.tick(60)










