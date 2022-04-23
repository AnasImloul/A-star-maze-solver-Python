from Node import Node
from Heap import MinHeap
import pygame

class Solver:
    def __init__(self,grid,sprites):
        self.grid = grid
        
        self.visited = set()
        
        self.heap = MinHeap(grid.slots*grid.slots, key = lambda node : (node.linearDistance, node.toEnd))
        
        self.nodeSize = int(self.grid.size/self.grid.slots)
        
        self.activeNodes = []
            
        self.moves = [(0,1),(1,0),(-1,0),(0,-1)]
        
        self.autoplay = False
        
        self.centralFont = pygame.font.SysFont("Arial", self.nodeSize//2)
        self.sideFont = pygame.font.SysFont("Arial", self.nodeSize//6)
        
        self.start = (0, 0)
        self.end = (self.grid.slots - 1, self.grid.slots - 1)
        
        self.next_step = False 
        
        self.solved = False
        
        self.sprites = sprites
        
    
    def solve(self):
        
        if len(self.visited) == 0:
            distance_to_start = 0
            distance_to_end = ((self.end[0]-self.start[0])**2 + (self.end[1]-self.start[1])**2)**0.5
            
            
            
            node = Node(self.centralFont, self.sideFont, distance_to_start, distance_to_end, self.nodeSize, (255,0,0), self.start[1], self.start[1])
        
            self.sprites.add(node)
            
            self.activeNodes.append(node)
            
            self.heap.insert(node)
            
            self.visited.add(self.start)
            
        
        else:
            
            
            
            min_node = self.heap.remove()
                    
            
            
            for move in self.moves:
                x,y = min_node.x + move[0], min_node.y +  move[1]
                
                if x in range(self.grid.slots) and y in range(self.grid.slots) and self.grid[x][y] == 0 and (x,y) not in visited:
                
            node = Node(self.centralFont, self.sideFont,distance_to_start, distance_to_end, self.nodeSize, (255,0,0), min_cost_node[0], min_cost_node[1])
            
            self.sprites.add(node)
            
            self.activeNodes.append(node)
            
            self.visited.add((min_cost_node[0],min_cost_node[1]))
            
            print((min_cost_node[0],min_cost_node[1]))
            
            if (min_cost_node[0],min_cost_node[1]) == self.end:
                self.grid.control.solve = False
                self.grid.control.state = self.grid.control.add_wall
                self.solved = True
                    
                    
    def render(self,screen):
       
        for node in self.activeNodes:
            node.render()
                    
                    
                    
    def reset(self):
        self.visited = set()
        self.activeNodes = []
        
        self.sprites.empty()
                    
                    
                    
                    
                    
                    
            
