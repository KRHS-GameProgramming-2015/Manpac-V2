import sys, pygame, math

class Norb():
    def __init__(self, pos=[0,0]):
        self.image = pygame.image.load("Norb/Norb.png")
        self.image = pygame.transform.scale(self.image, [25,25])
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        self.living = True
        self.value = 10
        self.kind = "normal"
        
    def update(self, size):
        pass


class Eorb(Norb):
    def __init__(self, pos=[0,0]):
        Norb.__init__(self,pos)
        self.living = True
        self.value = 25
        self.kind = "energizer"


        self.images = [pygame.transform.scale(pygame.image.load("Eorb/Eorb.png"),[40,40]),
                        pygame.transform.scale(pygame.image.load("Eorb/fEorb.png"),[40,40])]
        
        
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
    
    def update(self, size):
        self.animate()

class Fruit():
    def __init__(self, pos=[0,0]):
        self.image = pygame.image.load("Fruit/Cherry.png")
        self.image = pygame.transform.scale(self.image, [25,25])
        self.rect = self.image.get_rect(center = pos)
        self.radius = self.rect.width/2 - 2
        self.living = True
        self.value = 75
        self.kind = "normal"
    
    def update(self, size):
        pass
