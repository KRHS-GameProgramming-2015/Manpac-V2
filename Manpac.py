import sys, pygame, math
from Ball import Ball

class PlayerBall(Ball):
    def __init__(self, maxSpeed, pos = [0,0]):
        Ball.__init__(self, ["pacman-open-right.png"], [0,0], pos)
        self.rightImages = [pygame.image.load("pacman-open-right.png"),
                            pygame.image.load("pacman-closed-right.png")]
                           
        self.leftImages = [pygame.image.load("pacman-open-left.png"),
                           pygame.image.load("pacman-closed-left.png")]
                           
        self.upImages = [pygame.image.load("pacman-closed-upwards.png"),
                              pygame.image.load("pacman-open-upwards.png")]
        
        self.downImages = [pygame.image.load("pacman-closed-downwards.png"),
                                pygame.image.load("pacman-open-downwards.png")]
        
        
        self.images = self.rightImages
        self.images = self.leftImages
        self.images = self.upwardsImages
        self.images = self.downwardsImages
        self.maxFrame = len(self.images)-1
        
        self.xDirection = "right"
        self.yDirection = "none"
        
        self.maxSpeedx = maxSpeed[0]
        self.maxSpeedy = maxSpeed[1]
    
    def collideScreen(self, size):
        width = size[0]
        height = size[1]
        
        if not self.didBounceX:
            if self.rect.left < 0 or self.rect.right > width:
                self.speedx = -self.speedx
                self.didBounceX = True
                self.move()
                self.speedx = 0
        if not self.didBounceY:
            if self.rect.top < 0 or self.rect.bottom > height:
                self.speedy = -self.speedy
                selfdidBounceY = True
                self.move()
                self.speedy = 0
    
    def go(self, direction):
        if direction == "up":
            self.yDirection = "up"
            self.speedy = -self.maxSpeedy
            if self.xDirection == "right":
                self.images = self.upRightImages
            elif self.xDirection == "left":
                selfimages = self.upLeftImages
            else:
                self.images = self.upwardsImages
        elif direction == "down":
            self.speedy = self.maxSpeedy
            self.images = self.downwardsImages
        
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
            
            
            
