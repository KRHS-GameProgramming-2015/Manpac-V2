import sys, pygame, math, random
from Wall import *

pygame.init()

clock = pygame.time.Clock()

width = 700 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

screen = pygame.display.set_mode(size)

walls = [Wall([0,0],[800,50]), #0
         Wall([0,50],[50,300]),
         Wall([0,400],[50,650]),
         Wall([0,650],[700,700]),
         Wall([650,400],[700,650]),
         Wall([650,50],[700,300]), #5
         Wall([650,50],[700,300]), 
         Wall([650,50],[700,300]), 
         Wall([650,50],[700,300]), 
         Wall([650,50],[700,300]), 
         Wall([650,50],[700,300]), #10 
         ]
         
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
    
    bgColor = r,g,b
    screen.fill(bgColor)
    for wall in walls:
        screen.blit(wall.image, wall.rect)
    pygame.display.flip()
    clock.tick(60) 
