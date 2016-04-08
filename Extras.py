import sys, pygame, math

class Norb(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], blockSize = 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Norb/Norb.png")
        self.image = pygame.transform.scale(self.image, [blockSize/2,blockSize/2])
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        self.living = True
        self.value = 10
        self.kind = "normal"
        
    def update(*args):
        pass


class Eorb(Norb):
    def __init__(self, pos=[0,0], blockSize = 50):
        Norb.__init__(self, pos, blockSize)
        self.living = True
        self.value = 25
        self.kind = "energizer"

        self.images = [pygame.transform.scale(pygame.image.load("Eorb/Eorb.png"),[2*blockSize/3,2*blockSize/3]),
                        pygame.transform.scale(pygame.image.load("Eorb/fEorb.png"),[2*blockSize/3,2*blockSize/3])]
        
        self.frame = 0
        self.maxFrame = len(self.images)-1
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        
        self.timer = 0
        self.timerMax = .2* 60
        
    def animate(self):
        if self.timer < self.timerMax:
            self.timer += 1
        else:
            self.timer = 0
            if self.frame < self.maxFrame:
                self.frame += 1
            else:
                self.frame = 0
        self.image = self.images[self.frame]
    
    def update(*args):
        self = args[0]
        self.animate()

class Fruit(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], blockSize = 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Fruit/Cherry.png")
        self.image = pygame.transform.scale(self.image, [blockSize/2,blockSize/2])
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        self.living = True
        self.value = 75
        self.kind = "normal"
    
    def update(*args):
        pass
