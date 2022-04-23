import pygame
from Control import Control
from solver import Solver

class Grid:
    def __init__(self,size,slots,sprites):
        self.size = size
        self.slots = slots
        self.array = [[0 for i in range(slots)] for j in range(slots)]
        
        self.solver = Solver(self,sprites)
        
        self.control = Control(self,self.solver)
        
    
    
    
    def castPos(self,pos):
        x,y = int(pos[0]/(self.size/self.slots)), int(pos[1]/(self.size/self.slots))
        return x,y
    
    
            
      

    
    def render(self,screen):
        slot_size = (self.size / self.slots)
        
        for i in range(self.slots):
            for j in range(self.slots):
                if self.array[i][j]==1:
                    x = i*slot_size
                    y = j*slot_size 
                    
                    pygame.draw.rect(screen,(0,0,0),((x,y),(slot_size - 1,slot_size - 1)))
        
        
        for i in range(self.slots + 1):
            x = ((self.size-1) / self.slots)*i
            pygame.draw.line(screen,(0,0,0),(x,0),(x,self.size))
        
        for j in range(self.slots + 1):
            y = ((self.size-1) / self.slots)*j
            pygame.draw.line(screen,(0,0,0),(0,y),(self.size,y))
    
    
    def update(self,screen,events):
        self.control.update(events)
        self.solver.render(screen)
        self.render(screen)
        
    
    
    
    
    def __getitem__(self,pos):
        x,y = pos[0] / (self.size/self.slots) , pos[1] / (self.size/self.slots)
       
        return self.array[int(x)][int(y)]
        
    
    def __setitem__(self,pos,value):
        x,y = pos[0] / (self.size/self.slots) , pos[1] / (self.size/self.slots)
        self.array[int(x)][int(y)] = value
    