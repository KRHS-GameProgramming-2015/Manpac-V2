import pygame_sdl2
pygame_sdl2.import_as_pygame()

import pygame
import os
import random
import math
from Ball import Ball

def save_state(balls):
    """
    Saves the game state.
    """
    stateString = ""
    with open("state.txt", "w") as f:
        for ball in balls:
            stateString += "{} {} {} {} {}".format(ball.imageFile,
                                                   ball.speedx,
                                                   ball.speedy,
                                                   ball.rect.centerx,
                                                   ball.rect.centery)
            stateString += '\n'
        f.write(stateString)

def load_state():
    try:
        objects = []
        with open("state.txt", "r") as f:
            for line in f.read():
                f, sx, sy, x, y = line.split()
                objects += Ball(f, [int(sx), int(sy)], [int(x), int(y)])
        return objects
    except:
        return None

def delete_state():
    if os.path.exists("state.txt"):
        os.unlink("state.txt")

def main():
    pygame.init()
    
    clock = pygame.time.Clock()
    infoObject = pygame.display.Info()
    
    #print infoObject.current_w
    

    width = infoObject.current_w 
    height = infoObject.current_h
    size = width, height

    bgColor = r,g,b = 0, 0, 0
    
    screen = pygame.display.set_mode(size)
    pygame.display.set_mode()

    balls = load_state()
    delete_state()
    
    if balls == None:
        balls = []
    
    ballTimer = 0
    ballTimerMax = .75 * 60
    
    done = False
    sleeping = False
    
    font = pygame.font.Font("DejaVuSans.ttf", 124)
    text = font.render("Start", True, (255, 255, 255, 255))
    textRect = text.get_rect(center = (width/2, height/2))
    
    while not done:
        for event in pygame.event.get():
            text = font.render(str(event.type), True, (255, 255, 255, 255))
            if event.type == pygame.QUIT: 
                done = True
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_AC_BACK:
                done = True
            elif event.type == pygame.APP_WILLENTERBACKGROUND:
                # The app is about to go to sleep. It should save state, cancel
                # any timers, and stop drawing the screen until an APP_DIDENTERFOREGROUND
                # event shows up.
                save_state(balls)
                sleeping = True
            elif event.type == pygame.APP_DIDENTERFOREGROUND:
                # The app woke back up. Delete the saved state (we don't need it),
                # restore any times, and start drawing the screen again.
                delete_state()
                sleeping = False
                # For now, we have to re-open the window when entering the
                # foreground.
                screen = pygame.display.set_mode((1280, 720))
       
        if not sleeping:
            ballTimer += 1
            if ballTimer >= ballTimerMax:
                ballTimer = 0
                ballSpeed = [random.randint(-5, 5),
                             random.randint(-5, 5)]
                ballPos = [random.randint(100, width-100),
                             random.randint(100, height-100)]
                balls += [Ball("ball.png",ballSpeed,ballPos)]
                save_state(balls)
            
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
            screen.blit(text, textRect)
            pygame.display.flip()
            clock.tick(60)
            
        if done:
            break

if __name__ == "__main__":
    main()








