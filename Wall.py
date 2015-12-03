import sys, pygame, math

class Wall():
    def __init__(self, topLeft, bottomRight):
        width = bottomRight[0]-topLeft[0]
        height = bottomRight[1]-topLeft[1]
        self.image = pygame.image.load("Wall/wall.png")
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(topleft = topLeft)
