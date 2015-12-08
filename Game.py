import sys, pygame, math, random
from Wall import *
from Ghost import *

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
            
    for ghost in ghosts:
        ghost.update(size)
        for wall in walls:
            ghost.collideWall(wall)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for ghost in ghosts:
        screen.blit(ghost.image, ghost.rect)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60) 
