import sys, pygame, math, random
from Wall import *
from Ghost import *
from Manpac import *
from Extras import *
from Score import *

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    ghosts = [Ghost("purple", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("blue", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("green", [random.randint(250, 450),random.randint(250, 450)])]

    player = Manpac([7,7], (602,602))
    
    ghosts = [Ghost("purple", [random.randint(5, 8)*50+25,random.randint(5, 8)*50+25]),
          Ghost("blue", [random.randint(5, 8)*50+25,random.randint(5, 8)*50+25]),
          Ghost("green", [random.randint(5, 8)*50+25,random.randint(5, 8)*50+25])]

    score = Score("Score: ", (125,25))
    lives = Score("Lives: ", (125,675))
    while player.living and len(orbs) > 0:
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
                    
        player.update(size)
        
        score.update(player.score)
        lives.update(player.lives)
        
        for wall in walls:
            player.collideWall(wall)
                    
        for ghost in ghosts:
            ghost.update(size)
            for wall in walls:
                ghost.collideWall(wall)
            if ghost.living:
                if player.collideObject(ghost):
                    if ghost.energized:
                        ghost.die()
                    else:
                        player.die() 
                        player.rect.center = (625,625)
        
        for orb in orbs:
            orb.update(size)
            if player.collideObject(orb):
                player.score += orb.value 
                if orb.kind == "energizer":
                    for ghost in ghosts:
                        ghost.weaken()
                orb.living = False
                print player.score
        
        for orb in orbs:
            if not orb.living:
                orbs.remove(orb)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        for orb in orbs:
            screen.blit(orb.image, orb.rect)
        screen.blit(player.image, player.rect)
        for ghost in ghosts:
            if ghost.living:
                screen.blit(ghost.image, ghost.rect)
        for wall in walls:
            screen.blit(wall.image, wall.rect)
        screen.blit(score.image,score.rect)
        screen.blit(lives.image,lives.rect)
        pygame.display.flip()
        clock.tick(60) 
        print len(orbs)
        if len(orbs) == 1:
            print orbs[0].rect.center
        
    while not player.living:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Manpac([7,7], (602,602))
                
        bg = pygame.image.load("MenuStuff/GameOver.png")
        bgrect = bg.get_rect()
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60) 
        
    while len(orbs) <= 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    player = Manpac([7,7], (602,602))
                    orbs += [Norb([75,75])]
                
        bg = pygame.image.load("MenuStuff/Win screen.png")
        bgrect = bg.get_rect()
        
        bgColor = r,g,b
        screen.fill(bgColor)
        screen.blit(bg, bgrect)
        pygame.display.flip()
        clock.tick(60) 
