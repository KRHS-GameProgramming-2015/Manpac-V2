import sys, pygame, math, random
from Wall import *
from Ghost import *
from Manpac import *
from Extras import *
from Score import *
from Level import *

pygame.init()

clock = pygame.time.Clock()

width = 1000 
height = 700
size = width, height

bgColor = r,g,b = 0, 0, 0

ghosts = pygame.sprite.Group()
walls = pygame.sprite.Group()
players = pygame.sprite.Group()
extras = pygame.sprite.Group()
hud = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ghost.containers = (ghosts, all)
Wall.containers = (walls, all)
Manpac.containers = (players, all)
Eorb.containers = (extras, all)
Norb.containers = (extras, all)
Fruit.containers = (extras, all)
Score.containers = (hud, all)

screen = pygame.display.set_mode(size)

level = Level("Levels/Map33")

while True:
    player = Manpac([7,7], (602,602))
    
    score = Score("Score: ", 0, (125,25))
    lives = Lives("Lives: ", 3,  (125,675))
    while player.living:
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
        
        all.update(size, player.lives)
        
        playersHitsWalls = pygame.sprite.groupcollide(players, walls, False, False)
        
        for p in playersHitsWalls:
            for wall in playersHitsWalls[p]:
                p.collideWall(wall)
        
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen) 
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
