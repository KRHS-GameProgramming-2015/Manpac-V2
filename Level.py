import pygame, sys, math, random
from Wall import *
from Extras import *

class Level():
    def __init__(self, lev, sizeX, sizeY):
        #self.loadLevel(lev)
        self.loadAllLevels(lev, sizeX, sizeY)
    
    def loadAllLevels(self, lev, sizeX, sizeY):
        for fy in range(sizeY):
            for fx in range(sizeX):
                fileName = lev+str(fx+1)+str(fy+1)+".lvl"
                print fileName
                
                self.blockSize = 15
                screenHeight = 14*self.blockSize
                screenWidth = 20*self.blockSize
                
                file = open(fileName, 'r')
                lines = file.readlines()
                file.close()
                
                newlines = []
                for line in lines:
                    newline = ""
                    for c in line:
                        if c != '\n':
                            newline+= c
                    newlines += [newline]
                lines = newlines

                for line in lines:
                    print line
                    
                for y, line in enumerate(lines):
                    for x, c in enumerate(line):
                        if c == '#':
                            Wall([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                
                fileName = lev+str(fx+1)+str(fy+1)+".xta"

                file = open(fileName, 'r')
                lines = file.readlines()
                file.close()
                
                newlines = []
                for line in lines:
                    newline = ""
                    for c in line:
                        if c != '\n':
                            newline+= c
                    newlines += [newline]
                lines = newlines

                for line in lines:
                    print line
                    
                for y, line in enumerate(lines):
                    for x, c in enumerate(line):
                        if c == '.':
                            Norb([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
                            
                            Fruit([self.blockSize*x+self.blockSize/2+fx*screenWidth,
                                  self.blockSize*y+self.blockSize/2+fy*screenHeight],
                                  self.blockSize)
            
if __name__ == "__main__":
    pygame.init()

    clock = pygame.time.Clock()

    width = 15*20*3
    height = 15*14*3
    size = width, height

    bgColor = r,b,g = 0,0,0

    screen = pygame.display.set_mode(size)
    
    boundries = pygame.sprite.Group()
    orbs = pygame.sprite.Group()
    all = pygame.sprite.OrderedUpdates()
    
    Wall.containers = (boundries, all)
    Norb.containers = (orbs, all)
    
    myLev = Level("Levels/Map", 3,3)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    for s in all.sprites():
                        s.kill()
                    myLev = Level("Levels/Map", 3,3)
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen)
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
        
    