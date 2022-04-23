import pygame

from time import time, sleep
from Linkedlist import linkedlist
from Node import Node


SLEEP_REDO_UNDO = 0.02





class Control:
   
    
    
    def __init__(self,grid,solver):
        self.state = self.add_wall
        
        self.states = [self.add_wall,self.remove_wall,self.undo,self.redo,self.reset,self.solve]
        
        self.grid = grid
        self.solver = solver
        
        self.updates = linkedlist()
        
        self.last_updated = None
        
        #mouse is down ?
        self.mouse = False      
                
        # redo[0] = redo button clicked, redo[1] = how many times redo are done, redo[2] time of initial button press
        self.redo = [False,0,time()]
              
        # redo[0] = redo button clicked, redo[1] = how many times redo are done, redo[2] time of initial button press
        self.undo = [False,0,time()]    
        
        #solve button is pressed ?
        self.solve = False
        
        #reset button is down
        self.reset = False
        
    
    
    
    
    
    def add_wall(self):
        
        if self.mouse and self.grid[pygame.mouse.get_pos()] == 0:
            
            mouse_pos = pygame.mouse.get_pos()
            
            self.grid[mouse_pos] = 1
            
            if self.last_updated != None:
                pass
                #self.grid.interpolate(self.last_updated, mouse_pos)
            
                
            self.last_updated = mouse_pos
            self.updates.push((mouse_pos,0,1))
            
            
    def remove_wall(self):
        if self.mouse and self.grid[pygame.mouse.get_pos()] == 1:
            self.grid[pygame.mouse.get_pos()] = 0
            self.updates.push((pygame.mouse.get_pos(),1,0))
            
    def redo(self):
        
        if self.redo[0] and (self.redo[1] == 0 or time() - self.redo[2] > 1) and self.updates.length > 0:
            pos,old_value,new_value = self.updates.next()
            
            self.grid[pos] = new_value
            
            self.redo[1] += 1
            sleep(SLEEP_REDO_UNDO)
            
            
    def undo(self):
        if self.undo[0] and (self.undo[1] == 0 or time() - self.undo[2] > 1) and self.updates.length > 0:
            pos,old_value,new_value = self.updates.previous()
            
            
            self.grid[pos] = old_value
            
            self.undo[1] += 1
            sleep(SLEEP_REDO_UNDO)
            
        
    def reset(self):
        if self.reset:
            self.grid.array = [[0 for i in range(self.grid.slots)] for j in range(self.grid.slots)]  
            self.updates = linkedlist()
        
            self.reset = False
            self.state = self.states[0]
            
            self.solver.reset()
        
    
    def solve(self):
        if self.solve:
            self.solver.solve()
    
    
    def input(self,events):
        
        for event in events:

            if event.type == pygame.MOUSEBUTTONDOWN :
                self.mouse = True
            
            if event.type == pygame.MOUSEBUTTONUP:
                self.mouse = False
                self.last_updated = None
            
                    
            if event.type == pygame.KEYDOWN:
                
                if event.key == pygame.K_3:
                    self.state = self.states[2]
                    self.undo = [True,0,time()]
                    
                    
                if event.key == pygame.K_4:
                    self.state = self.states[3]
                    self.redo = [True,0,time()]
                    
                    
                    
            if event.type == pygame.KEYUP:
                
                if event.key == pygame.K_1:
                    self.state = self.states[0]
                    
                if event.key == pygame.K_2:
                    self.state = self.states[1]
                
                if event.key == pygame.K_3:
                    self.state = self.states[0]
                    
                    
                if event.key == pygame.K_4:
                    self.state = self.states[0]
                    
                    
                if event.key == pygame.K_5:
                    self.state = self.states[4]
                    self.reset = True
                    
                if event.key == pygame.K_6:
                    self.state = self.states[5]
                    self.solve = True
                    self.solver.reset()
                    
    
    
    def update(self,events):
        
        self.input(events)
        self.state()
    
