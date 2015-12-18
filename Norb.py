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

