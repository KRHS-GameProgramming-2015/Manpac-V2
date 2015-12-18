import sys, pygame, math, random
from Wall import *
from Ghost import *
from Manpac import *
from Norb import *

pygame.init()

clock = pygame.time.Clock()

width = 700 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

ghosts = [Ghost("purple", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("blue", [random.randint(250, 450),random.randint(250, 450)]),
          Ghost("green", [random.randint(250, 450),random.randint(250, 450)])]

player = Manpac([7,7], (602,602))

orbs = [Norb([75,75]),
        Norb([100,75]),
        Norb([150,75]),
        Norb([200,75])]

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
                
    player.update(size)
    for wall in walls:
        player.collideWall(wall)
                
    for ghost in ghosts:
        ghost.update(size)
        for wall in walls:
            ghost.collideWall(wall)
        if player.collideObject(ghost):
            player.die() 
    
    for orb in orbs:
        orb.update(size)
        if player.collideObject(orb):
            if orb.kind == "normal": 
                orb.living = False
    
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
    pygame.display.flip()
    clock.tick(60) 
