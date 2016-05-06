import sys, pygame, math

class Manpac(pygame.sprite.Sprite):
    def __init__(self, maxSpeed, pos = [0,0]):
        playerSize = [35,35]
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rightImages = [pygame.transform.scale(pygame.image.load("Manpac/pacman-open-right.png"),playerSize),
                            pygame.transform.scale(pygame.image.load("Manpac/pacman-closed-right.png"),playerSize)]
                           
        self.leftImages = [pygame.transform.scale(pygame.image.load("Manpac/pacman-open-left.png"),playerSize),
                           pygame.transform.scale(pygame.image.load("Manpac/pacman-closed-left.png"),playerSize)]
                           
        self.upImages = [pygame.transform.scale(pygame.image.load("Manpac/pacman-closed-upwards.png"),playerSize),
                        pygame.transform.scale(pygame.image.load("Manpac/pacman-open-upwards.png"),playerSize)]
        
        self.downImages = [pygame.transform.scale(pygame.image.load("Manpac/pacman-closed-downwards.png"),playerSize),
                           pygame.transform.scale(pygame.image.load("Manpac/pacman-open-downwards.png"),playerSize)]
        
        
        self.images = self.rightImages
        self.frame = 0
        self.maxFrame = len(self.images)-1
        
        self.image = self.images[self.frame]
        self.rect = self.image.get_rect()
        self.radius = self.rect.width/2 - 2
        
        self.xDirection = "right"
        self.yDirection = "none"
        
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
        
        self.timer = 0
        self.timerMax = .25* 60
        
        self.didBounceX = False
        self.didBounceY = False
        
        self.rect = self.rect.move(pos)
        
        self.living = True
        self.lives = 3
        
       
        
        self.score = 0
        
    def die(self):
        self.lives -= 1
        self.lives
        if self.lives <= 0:
            self.living = False

    def update(*args):
        self = args[0]
        size = args[1]
        self.move()
        self.animate()
        self.collideScreen(size)
        
        
    
    def collideObject(self, other):
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    return True
        return False
    
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.center[0] < -1: 
                self.rect.center = (width, self.rect.center[1])
            elif self.rect.center[0] > width+1:
                self.rect.center = (0, self.rect.center[1])
                
    def collideWall(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.speedy = 0
    
    
    
        
    
                 
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
    
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        self.didBounceX = False
        self.didBounceY = False 
                     
    def go(self, direction):
        if direction == "up":
            self.yDirection = "up"
            self.speedy = -self.maxSpeedy
            self.images = self.upImages
        elif direction == "down":
            self.speedy = self.maxSpeedy
            self.images = self.downImages
        
        if direction == "right":
            self.speedx = self.maxSpeedx
            self.images = self.rightImages
        elif direction == "left":
            self.speedx = -self.maxSpeedx
            self.images = self.leftImages
            
            
        if direction == "stop up":
            self.speedy = 0
            self.yDirection = "none"
        elif direction == "stop down":
            self.speedy = 0
        
        if direction == "stop right":
            self.speedx = 0
        elif direction == "stop left":
            self.speedx = 0
            
    def distanceTo(self, pt):
        x1 = self.rect.center[0]
        y1 = self.rect.center[1]
        x2 = pt[0]
        y2 = pt[1]
        return math.sqrt((x1-x2)**2+(y1-y2)**2)
        
        
        
            
            
