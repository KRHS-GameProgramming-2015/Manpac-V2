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
unloaded = pygame.sprite.Group()
all = pygame.sprite.OrderedUpdates()

Ghost.containers = (ghosts, unloaded, all)
Wall.containers = (walls, unloaded, all)
Manpac.containers = (players, all)
Eorb.containers = (extras, unloaded, all)
Norb.containers = (extras, unloaded, all)
Fruit.containers = (extras, unloaded, all)
Score.containers = (hud, unloaded, all)
    


screen = pygame.display.set_mode(size)

files = os.listdir("Levels/")
for f in files:
    if f[-4:] == ".sav":
        os.remove("Levels/"+f)

lx = 1
ly = 1
level = Level("Levels/Map"+str(lx)+str(ly))

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
        
        if player.rect.center[0] > size[0]:
            lx += 1
            theScore = score.score
            theLives = lives.score
            level.saveLevel(extras)
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [0, player.rect.center[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Lives("Lives: ", theLives,  (125,675))
        elif player.rect.center[0] < 0:
            lx -= 1
            theScore = score.score
            theLives = lives.score
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [size[0], player.rect.center[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Lives("Lives: ", theLives,  (125,675))
        elif player.rect.center[1] > size[1]:
            ly += 1
            theScore = score.score
            theLives = lives.score
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly)) 
            player.rect.center = [player.rect.center[0], 0]
            score = Score("Score: ", theScore, (125,25))
            lives = Lives("Lives: ", theLives,  (125,675))
        elif player.rect.center[1] < 0:
            ly -= 1
            theScore = score.score
            theLives = lives.score
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [player.rect.center[0], size[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Lives("Lives: ", theLives,  (125,675))
            
        
        playersHitsWalls = pygame.sprite.groupcollide(players, walls, False, False)
        
        for p in playersHitsWalls:
            for wall in playersHitsWalls[p]:
                p.collideWall(wall)
                
                
        playersHitsextras = pygame.sprite.groupcollide(players, extras, False, False)
        
        for p in playersHitsextras:
            for extra in playersHitsextras[p]:
                score.increase(extra.value)
                if extra.kind == "energizer":
                    p.energize()
                    for ghost in ghosts.sprites():
                        ghost.weaken()
                extra.kill()
          
        ghostsHitsWalls = pygame.sprite.groupcollide(ghosts, walls, False, False)
        
        for ghost in ghostsHitsWalls:
            for wall in ghostsHitsWalls[ghost]:
                ghost.collideWall(wall)
                
        playersHitsGhosts = pygame.sprite.groupcollide(players, ghosts, False, False)
         
        for p in playersHitsGhosts:
            for ghost in playersHitsGhosts[p]:
                p.collideGhost(ghost)
                if ghost.collidePlayer(p):
                    score.increase(ghost.value)
                
                
        
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen) 
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
