import sys, pygame, math, random

class Ghost(pygame.sprite.Sprite):
    def __init__(self, name, pos=[0,0]):
        pygame.sprite.Sprite.__init__(self, self.containers)
        if name == "purple":
            self.imageliving = pygame.image.load("Ghost/purple.png")
            self.imageliving = pygame.transform.scale(self.imageliving,[45,45])
            self.maxSpeed = 3
        elif name == "blue":
            self.imageliving = pygame.image.load("Ghost/blue.png")
            self.imageliving = pygame.transform.scale(self.imageliving,[45,45])
            self.maxSpeed = 4
        elif name == "green":
            self.imageliving = pygame.image.load("Ghost/green.png")
            self.imageliving = pygame.transform.scale(self.imageliving,[45,45])
            self.speed = [0,0]
            self.maxSpeed = 3
        else:
            print "BAD NAME!!!!", name
            sys.exit()
        
        self.startPos = pos
        
        self.imagedead = pygame.image.load("Ghost/dead ghost.png")
        self.imagedead = pygame.transform.scale(self.imagedead,[45,45])
        
        self.image = self.imageliving
        self.rect = self.image.get_rect()
        
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
        
        self.energized = False
        self.energizedtimer = 0
        self.energizedtimerMax = 5* 60 
        
        self.deadtimer = 0 
        self.deadtimerMax = 3*60
    
    def update(self, size):
        self.move()
        self.collideScreen(size)
        
        if self.energizedtimer > 0:
            self.energizedtimer += 1
            if self.energizedtimer > self.energizedtimerMax:
                self.energizedtimer = 0
                self.energized = False 
                self.image = self.imageliving
                
        if self.deadtimer > 0:
            self.deadtimer += 1
            if self.deadtimer > self.deadtimerMax:
                self.deadtimer = 0
                self.respawn()
             
    def weaken(self):
        self.energized = True
        self.energizedtimer = 1
        self.image = self.imagedead
        
    def die(self):
        self.living = False
        self.deadtimer = 1
        
        
    def respawn(self):
        self.living = True
        self.image = self.imageliving
        self.rect.center = self.startPos
        self.energized = False
    
    def move(self):
        if random.randint(0,90) == 0:
            self.speed = [0,0]
            while self.speed == [0,0]:
                self.speedx = self.maxSpeed * random.randint(-1,1)
                self.speedy = self.maxSpeed * random.randint(-1,1)
                self.speed = [self.speedx, self.speedy]
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
                self.speedx = -self.speedx
                self.speedy = -self.speedy
                self.move()
                self.speed = [0,0]
                while self.speed == [0,0]:
                    self.speedx = self.maxSpeed * random.randint(-1,1)
                    self.speedy = self.maxSpeed * random.randint(-1,1)
                    self.speed = [self.speedx, self.speedy]
                return True
        return False
