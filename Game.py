import sys, pygame, math, random
from Wall import *
from Ghost import *
from Manpac import *
from Extras import *
from Score import *
from Level import *
from Background import *

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
Background.containers = (hud, all)

screen = pygame.display.set_mode(size)


while True:
    levelsLeft = ["11", "12", "13",
                  "21", "22", "23",
                  "31", "32", "33"]
    
    deadGhosts = {}
    
    files = os.listdir("Levels/")
    for f in files:
        if f[-4:] == ".sav":
            os.remove("Levels/"+f)
    lx = 1
    ly = 1
    level = Level("Levels/Map"+str(lx)+str(ly))
    
    player = Manpac([7,7], (602,602))
    
    score = Score("Score: ", 0, (125,25))
    lives = Score("Lives: ", 130,  (125,675)) #>>>>>>>>>>>>>>Make 3!!!
    while lives.score >= 0  and len(levelsLeft)>8: #>>>>>>>>>>>>>>Make 0!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("right")
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    player.go("stop up")
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    player.go("stop down")
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    player.go("stop left")
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    player.go("stop right")
            
        all.update(size, player.lives)
        
        if player.rect.center[0] > size[0]:
            lx += 1
            theScore = score.score
            theLives = lives.score
            if level.saveLevel(extras):
                print "LEVEL: ", level.lev[-2:], "??????????????????????????????"
                if level.lev[-2:] in levelsLeft:
                    levelsLeft.remove(level.lev[-2:])
                print len(levelsLeft)
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [0, player.rect.center[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Score("Lives: ", theLives,  (125,675))
        elif player.rect.center[0] < 0:
            lx -= 1
            theScore = score.score
            theLives = lives.score
            if level.saveLevel(extras):
                print "LEVEL: ", level.lev[-2:], "??????????????????????????????"
                if level.lev[-2:] in levelsLeft:
                    levelsLeft.remove(level.lev[-2:])
                print len(levelsLeft)
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [size[0], player.rect.center[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Score("Lives: ", theLives,  (125,675))
        elif player.rect.center[1] > size[1]:
            ly += 1
            theScore = score.score
            theLives = lives.score
            if level.saveLevel(extras):
                print "LEVEL: ", level.lev[-2:], "??????????????????????????????"
                if level.lev[-2:] in levelsLeft:
                    levelsLeft.remove(level.lev[-2:])
                print len(levelsLeft)
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly)) 
            player.rect.center = [player.rect.center[0], 0]
            score = Score("Score: ", theScore, (125,25))
            lives = Score("Lives: ", theLives,  (125,675))
        elif player.rect.center[1] < 0:
            ly -= 1
            theScore = score.score
            theLives = lives.score
            if level.saveLevel(extras):
                print "LEVEL: ", level.lev[-2:], "??????????????????????????????"
                if level.lev[-2:] in levelsLeft:
                    levelsLeft.remove(level.lev[-2:])
                print len(levelsLeft)
            for s in unloaded.sprites():
                s.kill()
            level = Level("Levels/Map"+str(lx)+str(ly))
            player.rect.center = [player.rect.center[0], size[1]]
            score = Score("Score: ", theScore, (125,25))
            lives = Score("Lives: ", theLives,  (125,675))
            
        
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
                if p.collideGhost(ghost):
                    p.kill()
                    player = Manpac([7,7], (602,602))
                    lives.decrease(1)
                    print lives.score
                if ghost.collidePlayer(p):
                    score.increase(ghost.value)
                    deadGhosts[ghost.name] = [ghost.startPos, 0]
                    ghost.kill()
        
        for ghost in deadGhosts:
            deadGhosts[ghost][1] += 1
            if deadGhosts[ghost][1] == 3*60:
                Ghost(ghost, deadGhosts[ghost][0])
                
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen) 
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)
    
    for s in all.sprites():
        s.kill()
    bg = Background("MenuStuff/GameOver.png")
    while lives.score < 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    bg.kill()
                    lives = Score("Lives: ", 3,  (125,675))
                
    for s in all.sprites():
        s.kill()
    bg = Background("MenuStuff/YouWin.png")
    while len(levelsLeft) <= 8: #>>>>>>>>>>>>>>Make 0!!!
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    bg.kill()
                    lives = Score("lives: ", 3,  (125,675))
        
        bgColor = r,g,b
        screen.fill(bgColor)
        dirty = all.draw(screen) 
        pygame.display.update(dirty)
        pygame.display.flip()
        clock.tick(60)        
        
        
