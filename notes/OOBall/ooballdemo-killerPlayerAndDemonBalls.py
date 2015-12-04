import sys, pygame, math, random
from Ball import *
from PlayerBall import *
pygame.init()

clock = pygame.time.Clock()

width = 800 
height = 600
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

balls = []
ballTimer = 0
ballTimerMax = .75 * 60

player = PlayerBall("pBall.png",[6,6],[width/2, height/2])

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            elif event.key == pygame.K_DOWN:
                player.go("down")
            elif event.key == pygame.K_LEFT:
                player.go("left")
            elif event.key == pygame.K_RIGHT:
                player.go("right")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            elif event.key == pygame.K_DOWN:
                player.go("stop down")
            elif event.key == pygame.K_LEFT:
                player.go("stop left")
            elif event.key == pygame.K_RIGHT:
                player.go("stop right")
    
    ballTimer += 1
    if ballTimer >= ballTimerMax:
        ballTimer = 0
        ballSpeed = [random.randint(-5, 5),
                     random.randint(-5, 5)]
        ballPos = [random.randint(100, width-100),
                     random.randint(100, height-100)]
        balls += [Ball(["ball.png",
                        "balla.png",
                        "ballb.png",
                        "ballc.png"],
                       ballSpeed,
                       ballPos)]
        #print len(balls), clock.get_fps()
    
    player.update(size)
    for ball in balls:
        ball.update(size)
    
    for first in balls:
        if first.collideBall(player):
            first.die()
        else:
            for second in balls:
                if first != second:
                    first.collideBall(second)
    
    for ball in balls:
        if not ball.living:
            balls.remove(ball)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ball in balls:
        screen.blit(ball.image, ball.rect)
    screen.blit(player.image, player.rect)
    pygame.display.flip()
    clock.tick(60)










