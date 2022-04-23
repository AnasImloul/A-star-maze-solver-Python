# Python3 implementation of Min Heap

import sys

class MinHeap:

    def __init__(self, maxsize,key = lambda x:x):
        self.maxsize = maxsize
        self.size = 0
        self.Heap = [0]*(self.maxsize + 1)
        self.Heap[0] = -1 * sys.maxsize
        self.FRONT = 1
        
        self.key = key

   
    def parent(self, pos):
        return pos//2

    
    def leftChild(self, pos):
        return 2 * pos

   
    def rightChild(self, pos):
        return (2 * pos) + 1

   
    def isLeaf(self, pos):
        return pos*2 > self.size

    
    def swap(self, fpos, spos):
        self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos]

    
    def minHeapify(self, pos):

        # If the node is a non-leaf node and greater
        # than any of its child
        if not self.isLeaf(pos):
            if (self.key(self.Heap[pos]) > self.key(self.Heap[self.leftChild(pos)]) or
            self.key(self.Heap[pos]) > self.key(self.Heap[self.rightChild(pos)])):

                # Swap with the left child and heapify
                # the left child
                if self.key(self.Heap[self.leftChild(pos)]) < self.key(self.Heap[self.rightChild(pos)]):
                    self.swap(pos, self.leftChild(pos))
                    self.minHeapify(self.leftChild(pos))

                # Swap with the right child and heapify
                # the right child
                else:
                    self.swap(pos, self.rightChild(pos))
                    self.minHeapify(self.rightChild(pos))

    # Function to insert a node into the heap
    def insert(self, element):
        if self.size >= self.maxsize :
            return
        self.size+= 1
        self.Heap[self.size] = element

        current = self.size

        while self.key(self.Heap[current]) < self.key(self.Heap[self.parent(current)]):
            self.swap(current, self.parent(current))
            current = self.parent(current)
        
        
    # Function to print the contents of the heap
    def Print(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : "+ str(self.Heap[i])+" LEFT CHILD : "+
                                str(self.Heap[2 * i])+" RIGHT CHILD : "+
                                str(self.Heap[2 * i + 1]))

    # Function to build the min heap using
    # the minHeapify function
    def minHeap(self):

        for pos in range(self.size//2, 0, -1):
            self.minHeapify(pos)

    
    # Function to remove and return the minimum
    # element from the heap
    def get(self):
        return self.Heap[self.FRONT]
       


    # Function to remove and return the minimum
    # element from the heap
    def remove(self):
        popped = self.Heap[self.FRONT]
        if isinstance(popped,int):
            return return 
             
        self.Heap[self.FRONT] = self.Heap[self.size]
        self.size-= 1
        self.minHeapify(self.FRONT)
        return popped







