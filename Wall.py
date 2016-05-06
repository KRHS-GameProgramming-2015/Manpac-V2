import sys, pygame, math

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, blockSize):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = pygame.image.load("Wall/wall.png")
        self.image = pygame.transform.scale(self.image, (blockSize, blockSize))
        self.rect = self.image.get_rect(center = pos)
