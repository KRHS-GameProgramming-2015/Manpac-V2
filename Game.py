import sys, pygame, math, random
from Wall import *
from Ghost import *
from Manpac import *
from Norb import *
from Score import *

pygame.init()

clock = pygame.time.Clock()

width = 700 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

while True:
    ghosts = [Ghost("purple", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("blue", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("green", [random.randint(250, 450),random.randint(250, 450)])]

    player = Manpac([7,7], (602,602))

    orbs = [Norb([75,75]),
            Norb([125,75]),
            Norb([175,75]),
            Norb([225,75]),
            Norb([275,75]),
            Norb([325,75]),
            Norb([375,75]),
            Norb([425,75]),
            Norb([475,75]),
            Norb([525,75]),
            Norb([575,75]),
            Norb([625,75]),
            Norb([75,125]),
            Norb([75,175]),
            Norb([75,225]),
            Norb([75,275]),
            Norb([75,325]),
            Norb([75,375]),
            Norb([75,425]),
            Norb([75,475]),
            Norb([75,525]),
            Norb([75,575]),
            Norb([75,625]),
            Norb([125,275]),
            Norb([125,325]),
            Norb([125,375]),
            Norb([125,425]),
            Norb([175,225]),
            Norb([175,275]),
            Norb([175,425]),
            Norb([175,475]),
            Norb([225,175]),
            Norb([225,225]),
            Norb([225,275]),
            Norb([225,425]),
            Norb([225,475]),
            Norb([225,525]),
            Norb([225,625]),
            Norb([175,625]),
            Norb([125,625]),
            Norb([275,225]),
            Norb([275,125]),
            Norb([275,175]),
            Norb([275,275]),
            Norb([275,325]),
            Norb([275,375]),
            Norb([275,425]),
            Norb([275,475]),
            Norb([275,525]),
            Norb([275,575]),
            Norb([275,625]),
            Norb([325,125]),
            Norb([325,275]),
            Norb([325,425]),
            Norb([325,575]),
            Norb([325,625]),
            Norb([375,125]),
            Norb([375,275]),
            Norb([375,425]),
            Norb([375,575]),
            Norb([375,625]),
            Norb([425,125]),
            Norb([425,175]),
            Norb([425,225]),
            Norb([425,275]),
            Norb([425,325]),
            Norb([425,375]),
            Norb([425,425]),
            Norb([425,475]),
            Norb([425,525]),
            Norb([425,575]),
            Norb([425,625]),
            Norb([475,175]),
            Norb([475,225]),
            Norb([475,275]),
            Norb([475,425]),
            Norb([475,475]),
            Norb([475,525]),
            Norb([475,625]),
            Norb([525,225]),
            Norb([525,275]),
            Norb([525,425]),
            Norb([525,475]),
            Norb([525,625]),
            Norb([575,275]),
            Norb([575,325]),
            Norb([575,375]),
            Norb([575,425]),
            Norb([575,625]),
            Norb([625,125]),
            Norb([625,175]),
            Norb([625,225]),
            Norb([625,275]),
            Norb([625,325]),
            Norb([625,375]),
            Norb([625,425]),
            Norb([625,475]),
            Norb([625,525]),
            Norb([625,575]),
            Norb([625,625]),
            Eorb([515,167]),
            Eorb([170,170]),
            Eorb([167,515]),
            Eorb([517,516]),
            ]
            

    walls = [Wall([0,0],[800,50]), #0
             Wall([0,50],[50,300]),
             Wall([0,400],[50,650]),
             Wall([0,650],[700,700]),
             Wall([650,400],[700,650]),
             Wall([650,50],[700,300]), #5
             Wall([100,100],[250,150]), 
             Wall([100,150],[150,250]), 
             Wall([450,100],[600,150]), 
             Wall([550,150],[600,250]), 
             Wall([100,450],[150,600]), #10
             Wall([100,550],[250,600]), 
             Wall([450,550],[600,600]), 
             Wall([550,450],[600,600]), 
             Wall([150,300],[250,400]), 
             Wall([300,150],[400,250]), #15
             Wall([450,300],[550,400]), 
             Wall([300,450],[400,550]), #17
           ]  
    
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
            if player.collideObject(ghost):
                player.die() 
                player.rect.center = (625,625)
        
        for orb in orbs:
            orb.update(size)
            if player.collideObject(orb):
                player.score += orb.value 
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
