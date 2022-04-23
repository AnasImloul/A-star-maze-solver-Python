import pygame
from Grid import Grid
from Node import Node


#Global Variables
SIZE = 600
COLOR = (255,255,255)
SLOTS = 50


pygame.init()

screen = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('A* maze solver')

clock = pygame.time.Clock()



screen.fill((255,255,255))

sprites = pygame.sprite.Group()


grid = Grid(SIZE,SLOTS,sprites)


running = True


while running:  
    events = pygame.event.get()
    
    for event in events:
            if event.type == pygame.QUIT:
                running = False
    
 
    
    sprites.update()
    
    
            
    screen.fill((255,255,255))      
    
    sprites.draw(screen)  
    
    grid.update(screen,events)
    
    pygame.display.flip()
    
    
    
pygame.quit()
