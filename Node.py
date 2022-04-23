import pygame

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,200,0)


WIDTH = 500
HEIGHT = 500

class Node(pygame.sprite.Sprite):
    
    def __init__(self,centralFont, sideFont, distance_to_start, distance_to_end, size, color, x, y):
        # Call the parent class (Sprite) constructor  
        pygame.sprite.Sprite.__init__(self)
        
        
        self.x = x
        self.y = y
    
        self.toStart = distance_to_start
        self.toEnd = distance_to_end
        
        self.linearDistance = self.toStart + self.toEnd
        
        self.centralFont = centralFont
        
        self.sideFont = sideFont
        
        self.color = color
        self.size = size
            
        self.centralText = self.centralFont.render(str(self.linearDistance), 1, BLACK)
        self.leftText = self.sideFont.render(str(self.toStart), 1, BLACK)
        self.rightText = self.sideFont.render(str(self.toEnd), 1, BLACK)
        
        self.left = pygame.math.Vector2(size//6, size//6)
        self.right = pygame.math.Vector2(size - (size//6), size//6)
        self.center = pygame.math.Vector2(size//2, size - size//2.5)
        
        self.image = pygame.Surface([size, size])
        self.image.fill(self.color)
        
        self.rect = self.image.get_rect()
        self.rect.x = x*size
        self.rect.y = y*size
        
        
        # player movement 
        self.direction = pygame.math.Vector2()
        self.speed = 8
    
    
    def render(self):
        if self.color == WHITE:
            self.textColor = WHITE
        
        else:
            self.textColor = BLACK
            
        self.centralText = self.centralFont.render(str(self.linearDistance), 1, self.textColor)
        self.leftText = self.sideFont.render(str(self.toStart), 1, self.textColor)
        self.rightText = self.sideFont.render(str(self.toEnd), 1, self.textColor)
        
        
        self.image = pygame.Surface([self.size, self.size])
        self.image.fill(self.color)
    
        
        self.image.blit(self.centralText,
        [self.center.x - self.centralText.get_width()/2, self.center.y - self.centralText.get_height()/2])
        
        self.image.blit(self.leftText,
        [self.left.x - self.leftText.get_width()/2, self.left.y - self.leftText.get_height()/2])
        
        self.image.blit(self.rightText,
        [self.right.x - self.rightText.get_width()/2, self.right.y - self.rightText.get_height()/2])
        
        
      


    def update(self):
        self.render()