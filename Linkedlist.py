class node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.previous = None


class linkedlist:
    def __init__(self):
        self.length = 0
        self.first = None
        self.last = None
        self.current = None
        
        
    def push(self,value):
        temp = node(value)
        
        if self.length == 0:
            self.first = temp
            self.last = self.first
            
            
        else:
            temp.previous = self.last
            self.last.next = temp
            self.last = temp
            
        self.current = self.last
        
        self.length+=1
        
        
    def previous(self):
        
        if self.current.previous != None:
            self.current = self.current.previous
            return self.current.next.value
        
        else:
            return self.current.value
        
        
    def next(self):
        
        if self.current.next != None:
            self.current = self.current.next
            return self.current.previous.value
        
        else:
            return self.current.value