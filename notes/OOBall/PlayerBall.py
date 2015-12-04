import sys, pygame, math
from Ball import Ball

class PlayerBall(Ball):
    def __init__(self, images, maxSpeed, pos = [0,0]):
        Ball.__init__(self, images, [0,0], pos)
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
                
    def collideBall(self, other):
        print "I did it"
        if self.rect.right > other.rect.left and self.rect.left < other.rect.right:
            if self.rect.bottom > other.rect.top and self.rect.top < other.rect.bottom:
                if self.radius + other.radius > self.distanceTo(other.rect.center):
                    return True
        return False 
    
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeedy
        elif direction == "down":
            self.speedy = self.maxSpeedy
        if direction == "right":
            self.speedx = self.maxSpeedx
        elif direction == "left":
            self.speedx = -self.maxSpeedx
        
        if direction == "stop up":
            self.speedy = 0
        elif direction == "stop down":
            self.speedy = 0
        if direction == "stop right":
            self.speedx = 0
        elif direction == "stop left":
            self.speedx = 0
            
            
            
