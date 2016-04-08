import sys, pygame, math

class Score(pygame.sprite.Sprite):
    def __init__(self, text, pos = [0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.score = 0
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.image = self.font.render(self.text + str(self.score), 1, (0, 0, 0))
        self.rect = self.image.get_rect(center = pos)
        
    def update(*args):
        self = args[0]
        amount = args[2]
        if amount: 
            self.score = amount
        self.image = self.font.render(self.text + str(self.score), 1, (0, 0, 0))
        self.rect = self.image.get_rect(center = self.rect.center)
        
    def increase(self, amount=1):
        self.score += amount
    
    def decrease(self, amount=1):
        self.score -= amount
        
    def reset(self, amount=0):
        self.score = amount
