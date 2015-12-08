import sys, pygame, math, random

class Ghost():
    def __init__(self, name, pos=[0,0]):
        if name == "purple":
            self.image = pygame.image.load("Ghost/purple.png")
            self.image = pygame.transform.scale(self.image,[45,45])
            self.rect = self.image.get_rect()
            self.maxSpeed = 5
        elif name == "blue":
            self.image = pygame.image.load("Ghost/blue.png")
            self.image = pygame.transform.scale(self.image,[45,45])
            self.rect = self.image.get_rect()
            self.maxSpeed = 7
        elif name == "green":
            self.image = pygame.image.load("Ghost/green.png")
            self.image = pygame.transform.scale(self.image,[45,45])
            self.rect = self.image.get_rect()
            self.speed = [0,0]
            self.maxSpeed = 6
        else:
            print "BAD NAME!!!!", name
            sys.exit()
        
        self.speed = [0,0]
        while self.speed == [0,0]:
            self.speedx = self.maxSpeed * random.randint(-1,1)
            self.speedy = self.maxSpeed * random.randint(-1,1)
            self.speed = [self.speedx, self.speedy]
        
        self.radius = self.rect.width/2 - 2
        self.living = True
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.rect.center = pos
    
    def update(self, size):
        self.move()
        self.collideScreen(size)
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False
        
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
                
    def collideWall(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if not self.didBounceX:
                    if ((self.rect.center[0] < other.rect.center[0] and self.speedx > 0) or
                        (self.rect.center[0] > other.rect.center[0] and self.speedx < 0)):
                        self.speedx = -self.speedx
                        self.didBounceX = True
                        self.move()
                        oldspeedx = self.speedx
                        while self.speed == [0,0] or self.speedx == oldspeedx:
                            self.speedx = self.maxSpeed * random.randint(-1,1)
                            self.speed = [self.speedx, self.speedy]
                if not self.didBounceY:
                    if ((self.rect.center[1] < other.rect.center[1] and self.speedy > 0) or
                        (self.rect.center[1] > other.rect.center[1] and self.speedy < 0)):
                        self.speedy = -self.speedy
                        self.didBounceY = True
                        self.move()
                        oldspeedy = self.speedy
                        while self.speed == [0,0] or self.speedy == oldspeedy:
                            self.speedy = self.maxSpeed * random.randint(-1,1)
                            self.speed = [self.speedx, self.speedy]
                return True
        return False
