#!/usr/bin/python
## Name: Vivek Babu G R
## Date: 26-07-2018
## Assignment: Implementing the Stack DataStructure
## Question: Create a Class myStack to implement the working of Stack DataStructure.
######################################################################################

class myStack:
    capacity = 20
    def __init__(self):
        self.data = []
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def isFull(self):
        return self.count >= myStack.capacity

    def stackLength(self):
        return self.count

    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return False
    
    def push(self,dat):
        if not self.isFull():
            self.data.append(dat)
            self.count += 1
    
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            return False

class unlimStack:
    def __init__(self):
        self.data = []
        self.count = 0
        
    def isEmpty(self):
        return self.count == 0
    
    def stackLength(self):
        return self.count

    def stackPeek(self):
        if not self.isEmpty():
            return self.data[-1]
        else:
            return False
    
    def push(self,dat):
        self.data.append(dat)
        self.count += 1
    
    def pop(self):
        if not self.isEmpty():
            return self.data.pop()
        else:
            return False